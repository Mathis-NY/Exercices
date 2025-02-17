# import requests
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
# import numpy as np
# from datetime import datetime

# def main():
#     btc_amount, btc_buy_price, eth_amount, eth_buy_price, btc_buy_date, eth_buy_date = wallet_of_client()

#     print("\nLooking current prices from CoinGecko...")
#     btc_current_price, eth_current_price = current_price()
#     print(f"Current Bitcoin (BTC) price: ${btc_current_price}")
#     print(f"Current Ethereum (ETH) price: ${eth_current_price}")

#     btc_investment, eth_investment, total_investment = price_investment(btc_amount, btc_buy_price, eth_amount, eth_buy_price)

#     btc_value, eth_value, total_value = total_portfolio(btc_amount, btc_current_price, eth_amount, eth_current_price)

#     btc_allocation, eth_allocation = portfolio_allocation(btc_investment, eth_investment, total_investment)

#     btc_net_return = net_return(btc_value, btc_investment)
#     eth_net_return = net_return(eth_value, eth_investment)

#     print("\nPortfolio allocation (based on initial investment):")
#     print(f"BTC: {btc_allocation:.2f}%")
#     print(f"ETH: {eth_allocation:.2f}%")

#     print("\nNet return of the portfolio:")
#     print(f"BTC: {btc_net_return:.2f}%")
#     print(f"ETH: {eth_net_return:.2f}%")

#     print(f"\nThe current value of the portfolio is: ${total_value:.2f}")

#     profit_or_loss(total_value, total_investment)

#     create_portfolio_animation(btc_value, eth_value, btc_investment, eth_investment, total_value, btc_buy_date, eth_buy_date)

# def wallet_of_client():
#     while True:
#         try:
#             btc_amount = float(input("How much Bitcoin (BTC) do you have? "))
#             break
#         except ValueError:
#             print("Please enter a valid number.")

#     while True:
#         try:
#             btc_buy_price = float(input("At what price did you buy your Bitcoin (in dollars)? "))
#             break
#         except ValueError:
#             print("Please enter a valid number.")

#     while True:
#         try:
#             eth_amount = float(input("How much Ethereum (ETH) do you have? "))
#             break
#         except ValueError:
#             print("Please enter a valid number.")

#     while True:
#         try:
#             eth_buy_price = float(input("At what price did you buy your Ethereum (in dollars)? "))
#             break
#         except ValueError:
#             print("Please enter a valid number.")

#     while True:
#         try:
#             btc_buy_date = input("When did you buy your Bitcoin (YYYY-MM-DD)? ")
#             btc_buy_date = datetime.strptime(btc_buy_date, "%Y-%m-%d")
#             break
#         except ValueError:
#             print("Please enter a valid date (YYYY-MM-DD).")

#     while True:
#         try:
#             eth_buy_date = input("When did you buy your Ethereum (YYYY-MM-DD)? ")
#             eth_buy_date = datetime.strptime(eth_buy_date, "%Y-%m-%d")
#             break
#         except ValueError:
#             print("Please enter a valid date (YYYY-MM-DD).")

#     return btc_amount, btc_buy_price, eth_amount, eth_buy_price, btc_buy_date, eth_buy_date


# def current_price():
#     url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
#     response = requests.get(url)
#     data = response.json()
#     btc_price = data['bitcoin']['usd']
#     eth_price = data['ethereum']['usd']
#     return btc_price, eth_price


# def price_investment(btc_amount, btc_buy_price, eth_amount, eth_buy_price):

#     btc_investment = btc_amount * btc_buy_price
#     eth_investment = eth_amount * eth_buy_price
#     total_investment = btc_investment + eth_investment

#     return btc_investment, eth_investment, total_investment


# def total_portfolio(btc_amount, btc_current_price, eth_amount, eth_current_price):

#     btc_value = btc_amount * btc_current_price
#     eth_value = eth_amount * eth_current_price
#     total_value = btc_value + eth_value

#     return btc_value, eth_value, total_value


# def portfolio_allocation(btc_investment, eth_investment, total_investment):

#     btc_allocation = (btc_investment / total_investment) * 100
#     eth_allocation = (eth_investment / total_investment) * 100

#     return btc_allocation, eth_allocation


# def net_return(current_value, initial_investment):

#     return ((current_value - initial_investment) / initial_investment) * 100




# def profit_or_loss(total_value, total_investment):

#     profit_or_loss = total_value - total_investment

#     if profit_or_loss > 0:
#         print(f"\nYou made a profit of ${profit_or_loss:.2f} 🎉")
#     elif profit_or_loss < 0:
#         print(f"\nYou made a loss of ${abs(profit_or_loss):.2f} 😞")
#     else:
#         print("\nNo profit, no loss.")


# def create_portfolio_animation(btc_value, eth_value, btc_investment, eth_investment, total_value):
#     now = datetime.now()
#     btc_days_elapsed = (now - btc_buy_date).days
#     eth_days_elapsed = (now - eth_buy_date).days
#     total_days_elapsed = max(btc_days_elapsed, eth_days_elapsed)

#     # Time steps for the animation
#     steps = total_days_elapsed
#     x = np.arange(steps)

#     # Simulating the values
#     btc_values = np.linspace(btc_investment, btc_value, steps)
#     eth_values = np.linspace(eth_investment, eth_value, steps)
#     total_values = btc_values + eth_values

#     fig, ax = plt.subplots()
#     btc_line, = ax.plot([], [], lw=2, color='orange', label='BTC')
#     eth_line, = ax.plot([], [], lw=2, color='purple', label='ETH')
#     total_line, = ax.plot([], [], lw=2, color='green', label='Total Portfolio')

#     ax.set_xlim(0, steps)
#     ax.set_ylim(0, max(max(btc_values), max(eth_values), max(total_values)) * 1.1)
#     ax.set_xlabel('Time (Days since purchase)')
#     ax.set_ylabel('Portfolio Value (USD)')
#     ax.set_title('Portfolio Value Over Time')

#     ax.legend()

#     def init():
#         btc_line.set_data([], [])
#         eth_line.set_data([], [])
#         total_line.set_data([], [])
#         return btc_line, eth_line, total_line

#     def animate(i):
#         btc_line.set_data(x[:i], btc_values[:i])
#         eth_line.set_data(x[:i], eth_values[:i])
#         total_line.set_data(x[:i], total_values[:i])
#         return btc_line, eth_line, total_line

#     ani = animation.FuncAnimation(fig, animate, frames=steps, init_func=init, blit=True)

#     # Save the animation as a GIF
#     ani.save('portfolio_performance.gif', writer='pillow', fps=30)

#     plt.close(fig)  # Close the plot after the animation is done
#     print("Animation saved and program terminated.")

# if __name__ == "__main__":
#     main()






# # def graph_portfolio_performance(btc_value, eth_value, btc_investment, eth_investment, total_value):
# #     labels = ['Bitcoin', 'Ethereum', 'Total Portfolio Value']
# #     values = [btc_value, eth_value, total_value]
# #     initial_investment = [btc_investment, eth_investment, btc_investment + eth_investment]

# #     fig, ax = plt.subplots()

# #     x = range(len(labels))
# #     ax.bar(x, values, width=0.4, label="Current Value", align='center')
# #     ax.bar(x, initial_investment, width=0.4, label="Initial Investment", align='edge')

# #     ax.set_ylabel('Amount in USD')
# #     ax.set_title('Portfolio Performance')
# #     ax.set_xticks(x)
# #     ax.set_xticklabels(labels)
# #     ax.legend()

# #     plt.savefig('portfolio_performance.png')
# #     plt.close()


import requests
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from datetime import datetime

def main():
    btc_amount, btc_buy_price, eth_amount, eth_buy_price, btc_buy_date, eth_buy_date = wallet_of_client()

    print("\nLooking current prices from CoinGecko...")
    btc_current_price, eth_current_price = current_price()
    print(f"Current Bitcoin (BTC) price: ${btc_current_price}")
    print(f"Current Ethereum (ETH) price: ${eth_current_price}")

    btc_investment, eth_investment, total_investment = price_investment(btc_amount, btc_buy_price, eth_amount, eth_buy_price)

    btc_value, eth_value, total_value = total_portfolio(btc_amount, btc_current_price, eth_amount, eth_current_price)

    btc_allocation, eth_allocation = portfolio_allocation(btc_investment, eth_investment, total_investment)

    btc_net_return = net_return(btc_value, btc_investment)
    eth_net_return = net_return(eth_value, eth_investment)

    print("\nPortfolio allocation (based on initial investment):")
    print(f"BTC: {btc_allocation:.2f}%")
    print(f"ETH: {eth_allocation:.2f}%")

    print("\nNet return of the portfolio:")
    print(f"BTC: {btc_net_return:.2f}%")
    print(f"ETH: {eth_net_return:.2f}%")

    print(f"\nThe current value of the portfolio is: ${total_value:.2f}")

    profit_or_loss(total_value, total_investment)

    create_portfolio_animation(btc_value, eth_value, btc_investment, eth_investment, total_value, btc_buy_date, eth_buy_date)


def wallet_of_client():
    while True:
        try:
            btc_amount = float(input("How much Bitcoin (BTC) do you have? "))
            break
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            btc_buy_price = float(input("At what price did you buy your Bitcoin (in dollars)? "))
            break
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            eth_amount = float(input("How much Ethereum (ETH) do you have? "))
            break
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            eth_buy_price = float(input("At what price did you buy your Ethereum (in dollars)? "))
            break
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            btc_buy_date = input("When did you buy your Bitcoin (YYYY-MM-DD)? ")
            btc_buy_date = datetime.strptime(btc_buy_date, "%Y-%m-%d")
            break
        except ValueError:
            print("Please enter a valid date (YYYY-MM-DD).")

    while True:
        try:
            eth_buy_date = input("When did you buy your Ethereum (YYYY-MM-DD)? ")
            eth_buy_date = datetime.strptime(eth_buy_date, "%Y-%m-%d")
            break
        except ValueError:
            print("Please enter a valid date (YYYY-MM-DD).")

    return btc_amount, btc_buy_price, eth_amount, eth_buy_price, btc_buy_date, eth_buy_date


def current_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    btc_price = data['bitcoin']['usd']
    eth_price = data['ethereum']['usd']
    return btc_price, eth_price


def price_investment(btc_amount, btc_buy_price, eth_amount, eth_buy_price):
    btc_investment = btc_amount * btc_buy_price
    eth_investment = eth_amount * eth_buy_price
    total_investment = btc_investment + eth_investment
    return btc_investment, eth_investment, total_investment


def total_portfolio(btc_amount, btc_current_price, eth_amount, eth_current_price):
    btc_value = btc_amount * btc_current_price
    eth_value = eth_amount * eth_current_price
    total_value = btc_value + eth_value
    return btc_value, eth_value, total_value


def portfolio_allocation(btc_investment, eth_investment, total_investment):
    btc_allocation = (btc_investment / total_investment) * 100
    eth_allocation = (eth_investment / total_investment) * 100
    return btc_allocation, eth_allocation


def net_return(current_value, initial_investment):
    return ((current_value - initial_investment) / initial_investment) * 100


def profit_or_loss(total_value, total_investment):
    profit_or_loss = total_value - total_investment
    if profit_or_loss > 0:
        print(f"\nYou made a profit of ${profit_or_loss:.2f} 🎉")
    elif profit_or_loss < 0:
        print(f"\nYou made a loss of ${abs(profit_or_loss):.2f} 😞")
    else:
        print("\nNo profit, no loss.")


def create_portfolio_animation(btc_value, eth_value, btc_investment, eth_investment, total_value, btc_buy_date, eth_buy_date):
    # Calculating the time intervals
    now = datetime.now()
    btc_days_elapsed = (now - btc_buy_date).days
    eth_days_elapsed = (now - eth_buy_date).days
    total_days_elapsed = max(btc_days_elapsed, eth_days_elapsed)
    
    # Time steps for the animation
    steps = total_days_elapsed
    x = np.arange(steps)

    # Simulating the values
    btc_values = np.linspace(btc_investment, btc_value, steps)
    eth_values = np.linspace(eth_investment, eth_value, steps)
    total_values = btc_values + eth_values

    fig, ax = plt.subplots()
    btc_line, = ax.plot([], [], lw=2, color='orange', label='BTC')
    eth_line, = ax.plot([], [], lw=2, color='purple', label='ETH')
    total_line, = ax.plot([], [], lw=2, color='green', label='Total Portfolio')

    ax.set_xlim(0, steps)
    ax.set_ylim(0, max(max(btc_values), max(eth_values), max(total_values)) * 1.1)
    ax.set_xlabel('Time (Days since purchase)')
    ax.set_ylabel('Portfolio Value (USD)')
    ax.set_title('Portfolio Value Over Time')

    ax.legend()

    def init():
        btc_line.set_data([], [])
        eth_line.set_data([], [])
        total_line.set_data([], [])
        return btc_line, eth_line, total_line

    def animate(i):
        btc_line.set_data(x[:i], btc_values[:i])
        eth_line.set_data(x[:i], eth_values[:i])
        total_line.set_data(x[:i], total_values[:i])
        return btc_line, eth_line, total_line

    ani = animation.FuncAnimation(fig, animate, frames=steps, init_func=init, blit=True)

    # Save the animation as a GIF
    ani.save('portfolio_performance.gif', writer='pillow', fps=30)

    plt.close(fig)  # Close the plot after the animation is done
    print("Animation saved and program terminated.")


if __name__ == "__main__":
    main()
