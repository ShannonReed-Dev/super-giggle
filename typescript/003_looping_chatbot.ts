// Load env Variables----------------------------------------------------
import Anthropic from "@anthropic-ai/sdk";
import * as dotenv from "dotenv";
import * as readline from "readline";

//================================================
// Looping Chatbot
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

// Makes Request-----------------------
const chat = async (messages: Anthropic.MessageParam[]): Promise<string> => {
    const message = await client.messages.create({
        model,
        max_tokens: 1000,
        messages,
    });
    return (message.content[0] as Anthropic.TextBlock).text;
};


const main = async () => {
    const messages: Anthropic.MessageParam[] = [];

    // readline replaces Python's input() for getting user input in Node.js
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout,
    });

    const askQuestion = (prompt: string): Promise<string> =>
        new Promise((resolve) => rl.question(prompt, resolve));

    // Use a `while true` loop to run chatbot forever
    while (true) {
        // Get user input
        const userInput = await askQuestion("> ");
        console.log("> ", userInput);

        // Add user input to list of messages
        addUserMessage(messages, userInput);

        // Get Claude's response by calling claude with the chat function
        const answer = await chat(messages);

        // Add Claude's response to the list of messages
        addAssistantMessage(messages, answer);

        console.log("--------");
        console.log(answer);
    }
};

main();
