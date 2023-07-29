def maxProfit(prices) -> int:
    profit = 0
    buy = prices[0]
    for i in range(1, len(prices)):
        
        if buy > prices[i]:
            buy = prices[i]
            
        elif prices[i] - buy > profit:
            profit = prices[i] - buy
            
    return profit

def main():
    maxProfit([7, 15,1,5,3,6,4])

if __name__ == '__main__':
    main()