import input
import process
import output

def main():
    
    arr = input.fetch()
    product = process.operation(arr)
    output.show(product)

if __name__ == "__main__":
    main()