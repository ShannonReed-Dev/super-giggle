// Load env Variables----------------------------------------------------
import Anthropic from "@anthropic-ai/sdk";
import * as dotenv from "dotenv";


//================================================
// Structured Data
// Use message prefilling and stop sequences only to get three different commands in a single response
// There should not be any comments or explanation
//================================================


dotenv.config();


const client = new Anthropic();
const model = "claude-haiku-4-5";


// Helper Functions
const addUserMessage = (messages: Anthropic.MessageParam[], text: string): void => {
    messages.push({ role: "user", content: text });
};

const addAssistantMessage = (messages: Anthropic.MessageParam[], text: string): void => {
    messages.push({ role: "assistant", content: text });
};


const chat = async (messages: Anthropic.MessageParam[], stopSequences?: string[]): Promise<void> => {
    const params: Anthropic.MessageCreateParamsNonStreaming = {
        model,
        max_tokens: 1000,
        messages,
        stop_sequences: stopSequences,
    };

    const message = await client.messages.create(params);
    console.log((message.content[0] as Anthropic.TextBlock).text);
};


const main = async () => {
    const messages: Anthropic.MessageParam[] = [];

    const prompt = `
Generate three different sample AWS CLI commands. Each should be very short.
`;

    //===========================================================
    // addUserMessage(messages, prompt);

    // await chat(messages);

    // console.log(res.trim());
    //===========================================================



    //===========================================================
    // Use message prefilling and stop sequences only to get three different commands in a single response
    // There should not be any comments or explanation
    //===========================================================
    addUserMessage(messages, prompt);

    // Message prefilling is not just limited to characters
    addAssistantMessage(messages, "Here are all three commands in a single block without any comments :\n```bash");
    await chat(messages, ["```"]);
};

main();
