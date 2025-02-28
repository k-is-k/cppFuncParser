#include <iostream>
#include <vector>

using namespace std;

// グローバル関数
void hello() {
    // "Hello, world!" を出力する
    cout << "Hello, world!" << endl;
}

// 引数ありの関数
int add(int a, int b) {
    // 2つの整数を加算して返す
    return a + b;
}

// オーバーロードされた関数
double add(double a, double b) {
    // 2つの浮動小数点数を加算して返す
    return a + b;
}

// クラスの定義
class Math {
public:
    // クラスメンバ関数
    int multiply(int x, int y) {
        // 2つの整数を乗算して返す
        return x * y;
    }

    // クラスの静的メンバ関数
    static int square(int x) {
        // 整数の二乗を返す
        return x * x;
    }
};

// テンプレート関数
template <typename T>
T max_value(T a, T b) {
    // 2つの値のうち大きい方を返す
    return (a > b) ? a : b;
}

// メイン関数
int main() {
    // "Hello, world!" を出力する関数を呼び出す
    hello();
    // 3と5を加算して結果を出力する
    cout << "Add: " << add(3, 5) << endl;
    // 4と6を乗算して結果を出力する
    cout << "Multiply: " << Math().multiply(4, 6) << endl;
    // 5の二乗を計算して結果を出力する
    cout << "Square: " << Math::square(5) << endl;
    // 10と20のうち大きい方を出力する
    cout << "Max: " << max_value(10, 20) << endl;
    return 0;
}
