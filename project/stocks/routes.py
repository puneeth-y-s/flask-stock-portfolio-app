from flask import (
    current_app, render_template, request, session, 
    flash, redirect, url_for)
from . import stocks_blueprint
from pydantic import field_validator, BaseModel, ValidationError

class StockModel(BaseModel):
    """Class for parsing new stock data from a form"""
    stock_symbol: str
    number_of_shares: int
    purchase_price: float

    @field_validator('stock_symbol')
    def stock_symbol_check(cls, value):
        if not value.isalpha() or len(value) > 5:
            raise ValueError('Stock symbol must be 1-5 characters')
        return value.upper()

@stocks_blueprint.route("/")
def index():
    current_app.logger.info("calling the index function")
    return render_template("stocks/index.html")

@stocks_blueprint.route('/add_stock', methods = ['GET', 'POST'])
def add_stock():
    if request.method == "POST":
        try:
            stock_data = StockModel(
                stock_symbol=request.form["stock_symbol"],
                number_of_shares=request.form["number_of_shares"],
                purchase_price=request.form["purchase_price"]
            )
            print(stock_data)

            # Save the form data to the session object
            session["stock_symbol"] = stock_data.stock_symbol
            session["number_of_shares"] = stock_data.number_of_shares
            session["purchase_price"] = stock_data.purchase_price
            flash(f"Added new stock ({stock_data.stock_symbol})!", 'success')
            current_app.logger.info(f"Added new stock ({request.form['stock_symbol']})!")

            return redirect(url_for("stocks.list_stocks"))
        except ValidationError as e:
            print(e)
    return render_template("stocks/add_stock.html")

@stocks_blueprint.route("/stocks/")
def list_stocks():
    return render_template("stocks/stocks.html")