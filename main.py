import attendance as at
import scrape as s

if __name__ == '__main__':

    print("\nStarting...")
    df = s.getSheet()
    
    print("\nData Scraped, Analyzing...")
    at.calc(df)

    print("Done\n")