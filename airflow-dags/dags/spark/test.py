from pyspark import SparkContext

def main():
    # 創建SparkContext
    sc = SparkContext("local", "Simple Sum App")

    # 創建一個RDD（Resilient Distributed Dataset）
    numbers = sc.parallelize([1, 2, 3, 4, 5])

    # 定義一個函數來計算數字的總和
    def add(a, b):
        return a + b

    # 使用reduce操作計算總和
    total_sum = numbers.reduce(add)

    print(f"The sum of the numbers is: {total_sum}")

    # 停止SparkContext
    sc.stop()

if __name__ == "__main__":
    main()