// Load env Variables----------------------------------------------------
import Anthropic from "@anthropic-ai/sdk";
import * as dotenv from "dotenv";

//================================================
// Temperature
//================================================

dotenv.config();


const client = new Anthropic();
const model = "claude-haiku-4-5";


// Helper Functions
const addUserMessage = (messages: Anthropic.MessageParam[], text: string) => {
    messages.push({ role: "user", content: text });
};


const chat = async (
    messages: Anthropic.MessageParam[],
    prompt?: string,
    temperature: number = 1.0
): Promise<string> => {
    const params: Anthropic.MessageCreateParamsNonStreaming = {
        model,
        max_tokens: 1000,
        messages,
        temperature,
    };

    if (prompt) {
        params.system = prompt;
    }

    const message = await client.messages.create(params);
    return (message.content[0] as Anthropic.TextBlock).text;
};


const main = async () => {
    const bookIdeaPrompt = "Generate a one sentence book idea for kids between the ages 8 and 10";

    const messages: Anthropic.MessageParam[] = [];

    addUserMessage(messages, bookIdeaPrompt);

    const answer = await chat(messages, undefined, 0.0);

    console.log(answer);


    // with temperature=0.0 I always seem to get something about a young girl discovering her grandmother's antique music box
        // A young girl discovers that her grandmother's antique music box opens
        // a magical portal to a hidden kingdom where forgotten fairy tales
        // are real, and she must help the storybook characters fix
        // their mixed-up endings before the magic disappears forever.

    // Just because you dial up the temperature does not mean you will get dramatically different results
    // It just increases the chances of getting a different one


    // with temperature=1.0, results vary more with each run
    // after running a few times you may finally get a dramatically different result
};

main();
