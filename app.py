from flask import Flask, render_template, request

app = Flask(__name__)

def brute_force(arr):
    n = len(arr)
    max_sum = float('-inf')
    start, end = None, None  # Initialize start and end to None
    #For the nested loop it will be a time complexity of O(n^2), and space complexity of O(1)
    for i in range(n): # Outer loop that runs n times linearly from index 0 till n-1
        current_sum = 0
        for j in range(i, n): #Inner loop will run at most n times starting from j = i till n-1
            current_sum += arr[j]
            if current_sum > max_sum: #Ensuring that the sum is the maximum and updating accordingly
                max_sum = current_sum
                start = i
                end = j
                
    #then it should return the new indecies that have the sub-array with maximum sum and the its max-sum.
    return  max_sum, arr[start:end+1]
    
    
def divide_and_conquer(arr, low, high):
    if low == high:
        return arr[low], arr[low]

    mid = (low + high) // 2

    # Recursively find the maximum subarray sum in the left and right halves O(n/2)
    left_sum, left_subarray= divide_and_conquer(arr, low, mid)
    right_sum, right_subarray = divide_and_conquer(arr, mid + 1, high)

    # Find the maximum subarray sum that crosses the midpoint (Merging O(n))
    crossing_sum, crossing_subarray = max_crossing_sum(arr, low, mid, high)

    # Return the result with the maximum sum
    if left_sum >= right_sum and left_sum >= crossing_sum:
        return left_subarray, left_sum
    elif right_sum >= left_sum and right_sum >= crossing_sum:
        return right_subarray, right_sum
    else:
        return  crossing_sum,crossing_subarray

def max_crossing_sum(arr, low, mid, high):
    left_sum = float('-inf')
    sum_left = 0
    max_left_idx = mid
    #The total time complexity for the loops below is still considered as linear O(n)
    for i in range(mid, low - 1, -1): #This loop will run linearly, it will iterate till half of the main array therefore n/2.
        sum_left += arr[i]
        if sum_left > left_sum:
            left_sum = sum_left
            max_left_idx = i #Max on the left side

    right_sum = float('-inf')
    sum_right = 0
    max_right_idx = mid + 1

    for i in range(mid + 1, high + 1): #Similarly this loop will run linearly, it will iterate till half of the main array therefore n/2.
        sum_right += arr[i]
        if sum_right > right_sum:
            right_sum = sum_right
            max_right_idx = i #Max on the right side

    return left_sum + right_sum, arr[max_left_idx:max_right_idx + 1]


def classical_Dynamic_programming(arr):
    n = len(arr)
    maxSumEnding = [0] * n
    maxSumEnding[0] = arr[0]

    start, end = 0, 0

    for i in range(1, n):
        if maxSumEnding[i - 1] > 0:
            maxSumEnding[i] = arr[i] + maxSumEnding[i - 1]
        else:
            maxSumEnding[i] = arr[i]
            start = i  # Start a new subarray

        # Update end index if the current subarray sum is the maximum
        if maxSumEnding[i] > maxSumEnding[end]:
            end = i

    maxSubarraySum = max(maxSumEnding)
    subarray = arr[start:end + 1]
    return maxSubarraySum, subarray

def kadane_dynamic_programming(arr):
    n = len(arr)
    maxsumSoFar = arr[0]
    maxsumEndingHere = arr[0]
    start, end, tempStart = 0, 0, 0

    for i in range(1, n):
        if maxsumEndingHere + arr[i] < arr[i]:
            maxsumEndingHere = arr[i]
            tempStart = i
        else:
            maxsumEndingHere = maxsumEndingHere + arr[i]

        if maxsumSoFar < maxsumEndingHere:
            maxsumSoFar = maxsumEndingHere
            start = tempStart
            end = i

    subarray = arr[start:end + 1]
    return maxsumSoFar, subarray


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        print(request.form)  # Print the entire form data
        arr = list(map(int, request.form.get('arr', '').split(',')))
        print(arr)  # Print the parsed array

                
        match request.form['algorithm']:
            case 'bruteforce': result = brute_force(arr)
            case 'divideandconquer': result = divide_and_conquer(arr, 0, len(arr) - 1)
            case 'dynamicprogramming': result = classical_Dynamic_programming(arr)
            case 'kaden':  result = kadane_dynamic_programming(arr)

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
