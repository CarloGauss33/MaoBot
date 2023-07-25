export interface Quote {
    text: string;
    context: string;
}

export function selectRandomQuote(quotePath: string = './fixtures/quotes.json'): Quote {
  const quotes = require(quotePath);
  const randomIndex = Math.floor(Math.random() * quotes.length);
  return quotes[randomIndex];
}


