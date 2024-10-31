def financial_matrics():
    company_name = input('Company Name: ')
    price = input('Price: ')
    earning_per_share = input('Earning per share: ')
    book_value = input('Book value: ')

    pe_ratio = price/ earning_per_share
    pb_ratio = price/book_value