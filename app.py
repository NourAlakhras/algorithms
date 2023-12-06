from flask import Flask, render_template, request

app = Flask(__name__)

def brute_force(numbers, subarray_size):
    return [1, 2, 3]
def divide_and_conquer(numbers, subarray_size):
    return [1, 2, 3]
def dynamic_Programming(numbers, subarray_size):
    n = len(numbers)
    dp = [0] * n

    # Initialize the dynamic programming array
    dp[0] = numbers[0]

    for i in range(1, n):
        dp[i] = max(dp[i-1] + numbers[i], numbers[i])

    # Find the subarray with the maximum sum
    max_sum_index = dp.index(max(dp))
    max_subarray = numbers[max_sum_index - subarray_size + 1: max_sum_index + 1]

    return max_subarray

def greedy(numbers, subarray_size):
    start = 0
    current_sum = 0
    max_sum = float('-inf')
    max_subarray = []

    for end, num in enumerate(numbers):
        current_sum += num

        if end - start + 1 == subarray_size:
            if current_sum > max_sum:
                max_sum = current_sum
                max_subarray = numbers[start:end + 1]

            current_sum -= numbers[start]
            start += 1

    return max_subarray


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        number_array = list(map(int, request.form['numberArray'].split(',')))
        subarray_size = int(request.form['subarraySize'])
        algorithm = request.form['algorithm']

        
        match algorithm:
            case 'bruteforce': result = brute_force(number_array, subarray_size)
            case 'divideandconquer': result = divide_and_conquer(number_array, subarray_size)
            case 'dynamicprogramming': result = dynamic_Programming(number_array, subarray_size)
            case 'greedy':  result = greedy(number_array, subarray_size)

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
