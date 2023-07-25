import dotenv from 'dotenv';
import { Context, Telegraf, Format } from 'telegraf';
import { Update, Message } from 'typegram';
import { type Quote, selectRandomQuote } from './quotes';

dotenv.config();

interface MessageContext extends Context<Update> {
    content?: string;
    username?: string;
    messageId?: number;
}

const BOT_TOKEN = process.env.APP_TELEGRAM_BOT_TOKEN || '';
const bot = new Telegraf<MessageContext>(BOT_TOKEN);
const telegram = bot.telegram;

bot.start((ctx) => {
    ctx.reply('Maoism is dying, but we will revive it!');
});

bot.command('quote', (ctx) => {
    const quote = selectRandomQuote();
    ctx.replyWithHTML(`<i>${quote.text}</i>\n\n${quote.context}`);
});

bot.launch();
