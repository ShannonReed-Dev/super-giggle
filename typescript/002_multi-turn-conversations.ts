// Load env Variables----------------------------------------------------
import Anthropic from "@anthropic-ai/sdk";
import * as dotenv from "dotenv";

//================================================
// Multi-Turn Conversations
//================================================

dotenv.config();

// Create Client-------------------------------------------------------
const client = new Anthropic();
const model = "claude-haiku-4-5";


// Helper Functions-------------------------------------------------------------

const addUserMessage = (messages: Anthropic.MessageParam[], text: string) => {
    messages.push({ role: "user", content: text });
};

const addAssistantMessage = (messages: Anthropic.MessageParam[], text: string) => {
    messages.push({ role: "assistant", content: text });
};

const chat = async (messages: Anthropic.MessageParam[]): Promise<string> => {
    const message = await client.messages.create({
        model,
        max_tokens: 1000,
        messages,
    });
    return (message.content[0] as Anthropic.TextBlock).text;
};


const main = async () => {
    // When you run this code, Claude will process your request and return a response object containing the generated text along with metadata about the request.

    // Extracting the Response-----------------------------------------------------------

    // Start with an empty message list
    const messages: Anthropic.MessageParam[] = [];

    // Add the initial user question
    addUserMessage(messages, "Define quantum computing in one sentence");

    // Get Claude's response
    const answer = await chat(messages);

    // Response
    console.log(answer);

    // Add Claude's response to the conversation history
    addAssistantMessage(messages, answer);

    // Messages List
    console.log(messages);

    // Add a follow-up question
    addUserMessage(messages, "Write another sentence");

    // Get the follow-up response with full context
    const finalAnswer = await chat(messages);

    console.log(finalAnswer);
};

main();
