import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

df = pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year,country_code):

    year = year
    country_code = country_code.upper()
    
    query = f"(date >= '{year}-01-01') and (date <= '{year}-12-31') and (iso_a3 == '{country_code}')"

    df_result = df.query(query)

    mean_dollar_price = round(df_result['dollar_price'].mean(),2)

    return mean_dollar_price

def get_big_mac_price_by_country(country_code):
    
    country_code = country_code.upper()
    
    query = f"(iso_a3 == '{country_code}')"

    df_result = df.query(query)

    mean_dollar_price = round(df_result['dollar_price'].mean(),2)

    return mean_dollar_price

def get_the_cheapest_big_mac_price_by_year(year):

    year = year
    
    query = f"(date >= '{year}-01-01') and (date <= '{year}-12-31')"
    
    df_result = df.query(query)

    min_dollar_price =df_result['dollar_price'].idxmin()

    row = df_result.loc[min_dollar_price]
    result = f"{row['name']}({row['iso_a3']}): ${round(row['dollar_price'],2)}"
    
    return result

def get_the_most_expensive_big_mac_price_by_year(year):
    
    year = year
    
    query = f"(date >= '{year}-01-01') and (date <= '{year}-12-31')"
    
    df_result = df.query(query)

    max_dollar_price = df_result['dollar_price'].idxmax()
    
    row = df_result.loc[max_dollar_price]
    
    result = f"{row['name']}({row['iso_a3']}): ${round(row['dollar_price'],2)}"

    return result

if __name__ == "__main__":
    print(get_big_mac_price_by_year(input("Enter a Year: "),input("Enter your country code: ")))
    print(get_big_mac_price_by_country(input("Enter a country code: ")))
    print(get_the_cheapest_big_mac_price_by_year(2008))
    print(get_the_most_expensive_big_mac_price_by_year(2003))