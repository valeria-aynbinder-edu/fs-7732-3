import spacy

TEXT1 = """
Value versus growth? Sometimes, it’s hard to tell the difference. And sometimes, it may depend on what index you are using.
Is Microsoft a growth or value stock? Most investors would say it’s a growth stock, because it has the traditional characteristics of a growth stock: earnings are growing.
But Microsoft is now being classified as partly a growth stock by Standard & Poors, and partly a value stock.
What about Meta? It too was considered a classic growth stock. Not anymore. S&P now says it is 100% a value stock.
Is ExxonMobil a growth or value stock? It has for some time been associated with value, which has been associated with companies that paid high dividends, had a lower P/E ratio and usually a lower price to book ratio. But ExxonMobil is now 100% classified as a growth stock by S&P.
And not just Exxon: Chevon, ConocoPhillips, Williams, Coterra Energy, Marathon Oil, and EQT (all energy stocks) are now considered pure growth stocks.
"""

TEXT2 = """
Dr. Smith thinks that J.P. Morgan is a great bank and a good value stock hence you should buy it.
However you never know what will actually happen to the market, so you should always take risks into account
"""

TEXT3 = """
Apple is looking at buying U.K. startup for $1 billion
"""


if __name__ == '__main__':
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(TEXT3)


    for i, sentence in enumerate(doc.sents):
        # print(f"Sentence {i}: {sentence}")
        # for token in sentence:
        #     print(token.text, token.pos_)
        for ent in sentence.ents:
            print(ent.text, ent.label_)
