import React, {Component} from "react";
import { GetTradeProxy, DeleteTradeProxy, UpdateTradeProxy } from "./BackendProxy";

class Trades extends Component {

  constructor() {
    super();
    this.getProxy = new GetTradeProxy();
    this.deleteProxy = new DeleteTradeProxy();
    this.updateProxy = new UpdateTradeProxy();
    this.deleteProxy = new DeleteTradeProxy();
  }

  getTrades = () => {
    this.getProxy.getListOfTrades()
      .then(trades => console.log(trades))
      .catch(error => { throw error });
  }

  getTradesByPage = (page) => {
    this.getListOfTrades(page)
      .then(trades => console.log(trades))
      .catch(error => { throw error });
  }

  getTradeByID = (tradeID) => {
    tradeID = 'TEST101'
    this.getProxy.getTradeByID(tradeID)
      .then(trade => console.log(trade));
  }

  updateTrade = (tradeID) => {
    const exampleTrade = {
      date_of_trade: "2020-02-29 12:30",
      trade_id: "TEST101",
      product: "1",
      buying_party: "2",
      selling_party: "1",
      notional_amount: 1.0,
      quantity: 1.0,
      notional_currency: "USD",
      maturity_date: "2020-02-20",
      underlying_price: 1.0,
      underlying_currency: "USD",
      strike_price: 1.0
    };
    this.updateProxy.updateTrade(exampleTrade);
  }

  partiallyUpdateTrade = (tradeID) => {
    tradeID = "TEST101"
    const update = {
      buying_party: "7",
      selling_party: "7",
    }
    this.updateProxy.partiallyUpdateTrade(update, tradeID);
  }

  deleteTrade = (tradeID) => {
      this.deleteProxy.deleteTrade("TEST101");
  }

  render() {
    return (
      <div>
        <h2> This will be the editing/deleting/viewing trades page!</h2>
        <button onClick={this.updateTrade}>Update TEST101</button>
        <button onClick={this.partiallyUpdateTrade}>Partially Update TEST101</button>
        <button onClick={this.getTrades}>Get Trades</button>
        <button onClick={this.deleteTrade}>DELETE TEST101</button>
      </div>
    );
  }
}
export default Trades;