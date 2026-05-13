// Load env Variables----------------------------------------------------
import Anthropic from "@anthropic-ai/sdk";
import * as dotenv from "dotenv";


//================================================
// Structured Data
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


const chat = async (messages: Anthropic.MessageParam[], stopSequences?: string[]): Promise<string> => {
    const params: Anthropic.MessageCreateParamsNonStreaming = {
        model,
        max_tokens: 1000,
        messages,
        stop_sequences: stopSequences,
    };

    const message = await client.messages.create(params);
    return (message.content[0] as Anthropic.TextBlock).text;
};


const main = async () => {
    const userMessage = "Count from 1 to 10";

    const messages: Anthropic.MessageParam[] = [];
    //===========================================================
    // addUserMessage(messages, userMessage);

    // const res = await chat(messages, ["8"]);

    // console.log(res);

    // //===========================================================


    // // To generate structured data like JSON, Python code, or
    // // bulleted lists, you'll often run into a common problem:
    //     // Claude wants to be helpful and add explanatory text
    //     // around your content, but sometimes you need just
    //     // the raw data with nothing else.



    // addUserMessage(messages, "Generate a very short bridge rule as json");

    // const res = await chat(messages);

    // // Claude returns the JSON wrapped in markdown code blocks
    // // with explanatory text, users can't simply copy the
    // // entire response, they have to manually select
    // // just the JSON portion
    // console.log(res);
    // //===========================================================


    //===========================================================
    // Assistant Message Prefilling + Stop Sequences
    // Combine assistant message prefilling with stop sequences
    // to get exactly the content you want
    //===========================================================
    addUserMessage(messages, "Generate a very short bridge rule as json");

    // prefilled assistant message makes Claude
    // think it already started a markdown code block
    // So it thinks it already wrote out "```json",
    // so it continues by writing just the JSON content
    addAssistantMessage(messages, "```json");

    // Claude then tries to close the code block with ```,
    // but the stop sequence immediately ends generation
    const res = await chat(messages, ["```"]);

    console.log(res);


    //===========================================================
};

main();
