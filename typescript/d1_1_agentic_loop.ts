// Load env Variables----------------------------------------------------
import Anthropic from "@anthropic-ai/sdk";
import * as dotenv from "dotenv";

//================================================
// Agentic Loop - Calculator Agent
//================================================

dotenv.config();


// Create Client-------------------------------------------------------
const client = new Anthropic();
const model = "claude-haiku-4-5";


const tools: Anthropic.Tool[] = [{
    name: "calculate",
    description: "Evaluates a math expression and returns the result",
    input_schema: {
        type: "object",
        properties: {
            expression: {
                type: "string",
                description: "The math expression to evaluate, e.g. '24 * 7'"
            }
        },
        required: ["expression"]
    }
}];


// The actual function that runs when Claude calls the tool
// WARNING: eval() is only safe here because this is a learning context.
// In production, use a dedicated math parser library instead.
const calculate = (expression: string): number => {
    return eval(expression) as number;
};


// Initial user message - the question we want the agent to answer
const messages: Anthropic.MessageParam[] = [
    { role: "user", content: "What is 12 x 12?" }
];

const main = async () => {
    while (true) {
        const res = await client.messages.create({
            model,
            messages,
            tools,
            max_tokens: 1024,
        });

        // Stage 2: Claude is done - print the final answer and exit the loop
        if (res.stop_reason === "end_turn") {
            console.log((res.content[0] as Anthropic.TextBlock).text);
            break;
        }

        // Stage 2 (alternate): Claude wants to use a tool
        else if (res.stop_reason === "tool_use") {
            // Find the tool_use block in Claude's response
            const toolBlock = res.content.find(
                (b): b is Anthropic.ToolUseBlock => b.type === "tool_use"
            )!;

            // Stage 3: Run the tool locally with the inputs Claude provided
            const input = toolBlock.input as { expression: string };
            const result = calculate(input.expression);
            console.log(`Tool called: ${toolBlock.name}(${input.expression}) = ${result}`);

            // Stage 4: Append Claude's full response, then the tool result
            messages.push({ role: "assistant", content: res.content });
            messages.push({
                role: "user",
                content: [{
                    type: "tool_result",
                    tool_use_id: toolBlock.id,
                    content: String(result),
                }]
            });
        }
    }
};

main();
