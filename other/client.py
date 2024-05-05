import asyncio
import aiohttp

async def fetch(session, url, payload):
    async with session.post(url, json=payload) as response:
        return await response.json()

async def main():
    output_file = 'results.txt'
    tasks = []
    with open('numbers.txt', 'r') as file:
        lines = file.readlines()

    async with aiohttp.ClientSession() as session:
        for line in lines:
            parts = line.strip().split(',')
            if len(parts) != 3:
                print("Invalid input format in numbers.txt")
                return

            operation_code = int(parts[0])
            num1 = float(parts[1])
            num2 = float(parts[2])

            operations = {
                1: 'add',
                2: 'subtract',
                3: 'multiply',
                4: 'divide'
            }

            if operation_code not in operations:
                print("Invalid operation code in numbers.txt")
                return

            operation = operations[operation_code]

            payload = {
                'operation': operation,
                'num1': num1,
                'num2': num2
            }

            tasks.append((num1, num2, operation, fetch(session, url='http://localhost:5000/calculate', payload=payload)))

        with open(output_file, 'w') as f_out:
            for num1, num2, operation, task in tasks:
                try:
                    response = await task
                    if 'result' in response:
                        result_data = response['result']
                        output_line = f"Result: {num1} {operation} {num2} = {result_data}\n"
                        f_out.write(output_line)
                    else:
                        error = response.get('error', 'Unknown error')
                        output_line = f"Error: {error}\n"
                        f_out.write(output_line)
                except Exception as e:
                    print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
