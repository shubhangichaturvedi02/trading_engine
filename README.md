Order API
To buy or sell an instrument/stock, a buyer places a bid order in the exchange with the desired quantity(to buy) and a maximum price(bid
price) at which he/she is willing to buy, whereas a seller places an ask order with desired quantity(to sell) and a minimum price(ask price) at
which he/she is willing to sell.
When a bid offer/order matches an ask offer/order, a trade takes place. This is the core working of an exchange matching engine which
accepts Requests[to place(create), to modify(update), to cancel(delete)] an order, and matches them to create a transaction. It uses an
order book data structure.
What is a limit order book?

For this task, we’ll simulate an order api using which we can place, modify, or cancel an order. We’ll be able to get snapshots of currently
placed orders, as well as all the trades that have taken place so far. You’ll implement a data structure that maintains a limit order book and
takes actions as and when a request arrives.
Order matching means that a bid and ask are compatible for a trade to take place. The traded price is the one that's already present in the
book, meaning if a bid comes that matches the best ask then the ask price is taken for trade price. Similarly if an ask comes that matches
the best bid then the bid price is the traded price.
