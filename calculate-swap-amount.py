def calculate_swap(eth_balance, usd_balance, target_eth_ratio, min_eth_balance_after_swap=10):
   """
	Performs a swap between ETH and USD balances based on the given parameters.

	Args:
	    eth_balance (float): The current ETH balance.
	    usd_balance (float): The current USD balance.
	    target_eth_ratio (float): The desired ETH ratio.
	    min_eth_balance_after_swap (float, optional): The minimum ETH balance after the swap. Defaults to 10.

	Returns:
	    Tuple[float, float, int, str]: A tuple containing the updated ETH balance, updated USD balance, swap amount, and swap direction.

	Raises:
	    None.

	"""
    total_balance = eth_balance + usd_balance
    min_ratio_ETH = (MIN_SWAP_VALUE + min_eth_balance_after_swap) / total_balance
    max_ratio_ETH = (MAX_SWAP_VALUE + min_eth_balance_after_swap) / total_balance

    current_eth_ratio = eth_balance / total_balance
    print(f"ETH Ratio: {round(current_eth_ratio, 2)}")
    swap_direction = "ETH->USD"

    if current_eth_ratio >= target_eth_ratio:
        # Swap ETH to USD
        swap_direction = "ETH->USD"
        max_randomable = eth_balance - min_eth_balance_after_swap
        print(f"Max randomable ETH: {max_randomable}")

        if max_randomable < MIN_SWAP_VALUE:
            print("Swap amount ETH is less than minimum swap value --> CHANGE DIRECTION")
            swap_direction = "USD->ETH"
            max_randomable = usd_balance
    else:
        # Swap USD to ETH
        swap_direction = "USD->ETH"
        max_randomable = usd_balance #min(usd_balance, MAX_SWAP_VALUE)
        print(f"Max randomable USD: {max_randomable}")

        if max_randomable < MIN_SWAP_VALUE:
            print("Swap amount USD is less than minimum swap value --> CHANGE DIRECTION")
            # import pdb
            # pdb.set_trace()
            swap_direction = "ETH->USD"
            max_randomable = eth_balance - min_eth_balance_after_swap
            
    max_random_swap_value = min(max_randomable, MAX_SWAP_VALUE)
    print(f"Max randomable value: {max_random_swap_value}")
    
    swap_amount = random.randint(MIN_SWAP_VALUE, max_random_swap_value)

    if swap_direction == "ETH->USD":
        print(f"Swap {swap_amount}$ ETH -> USD")
        eth_balance -= swap_amount
        usd_balance += swap_amount
    else:
        print(f"Swap {swap_amount}$ USD -> ETH")
        eth_balance += swap_amount
        usd_balance -= swap_amount

    return eth_balance, usd_balance, swap_amount, swap_direction
