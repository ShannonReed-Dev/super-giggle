// Load env Variables----------------------------------------------------
import Anthropic from "@anthropic-ai/sdk";
import * as dotenv from "dotenv";
import * as readline from "readline";

//================================================
// System Prompting
//================================================

dotenv.config();


// Create Client-------------------------------------------------------
const client = new Anthropic();
const model = "claude-haiku-4-5";


// Helper Functions
const addUserMessage = (messages: Anthropic.MessageParam[], text: string) => {
    messages.push({ role: "user", content: text });
};

const addAssistantMessage = (messages: Anthropic.MessageParam[], text: string) => {
    messages.push({ role: "assistant", content: text });
};


//--------------------------------------------------------------------------------------System Prompt as argument------------------------------------------------------------------
// Makes Request-----------------------
const chat = async (messages: Anthropic.MessageParam[], prompt?: string): Promise<string> => {

// Doing it this way will allow you to call chat without a prompt if you want
// So both of these work
    // const answer = await chat(messages, tutorPrompt);
    // const answer = await chat(messages);

    const params: Anthropic.MessageCreateParamsNonStreaming = {
        model,
        max_tokens: 1000,
        messages,
    };

    if (prompt) {
        params.system = prompt;
    }

    const message = await client.messages.create(params);
    return (message.content[0] as Anthropic.TextBlock).text;
};
//----------------------------------------------------------------------------------------------

// Create the prompt
const seniorEngineerPrompt = `
    You are a senior TypeScript engineer. When asked to write a function, respond with only the function implementation. No prose, no explanations, no usage examples, no comments unless logic is non-obvious, no surrounding markdown commentary.

    Rules:
    - Output only the code block containing the function (and required imports).
    - Use the most concise idiomatic TypeScript that meets the request.
    - Include type annotations and a one-line JSDoc; omit everything else.
    - Do not restate the task, summarize the code, or suggest improvements.
    - If the request is ambiguous, ask one short clarifying question instead of guessing.
    `;

const main = async () => {
    const messages: Anthropic.MessageParam[] = [];

    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout,
    });

    const askQuestion = (prompt: string): Promise<string> =>
        new Promise((resolve) => rl.question(prompt, resolve));

    // Use a `while true` loop to run chatbot forever
    while (true) {
        const userInput = await askQuestion("> ");
        console.log("> ", userInput);

        addUserMessage(messages, userInput);

        const answer = await chat(messages, seniorEngineerPrompt);

        addAssistantMessage(messages, answer);

        console.log("--------");
        console.log(answer);
    }
};

main();
