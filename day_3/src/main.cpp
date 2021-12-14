#include <algorithm>
#include <array>
#include <bitset>
#include <fstream>
#include <iostream>
#include <numeric>
#include <string>
#include <string_view>
#include <vector>

constexpr int bit_length = 12;

const std::string uri = "/home/sonulen/wrk/advent_of_code/day_3/src/input.txt";

void print(const auto& iterable) {
    std::cout << "[";
    for (const auto& value : iterable) {
        std::cout << value << ", ";
    }
    std::cout << "]" << std::endl;
}

std::pair<int, int> calculate_counts(std::vector<std::string>& numbers,
                                     int                       symbol_index) {
    int zero_count = 0;
    int one_count  = 0;
    for (size_t index = 0; index < numbers.size(); index++) {
        if (numbers[index][symbol_index] == '0')
            zero_count++;
        else
            one_count++;
    }
    return {zero_count, one_count};
}

char calculate_oxygen_bit(std::vector<std::string>& numbers, int symbol_index) {
    auto [zero_count, one_count] = calculate_counts(numbers, symbol_index);
    return one_count >= zero_count ? '1' : '0';
}

char calculate_co2_bit(std::vector<std::string>& numbers, int symbol_index) {
    auto [zero_count, one_count] = calculate_counts(numbers, symbol_index);
    return zero_count > one_count ? '1' : '0';
}

long proceed(std::vector<std::string>& numbers) {
    std::vector<std::string> oxygen = numbers;
    std::vector<std::string> co2    = numbers;

    for (int i = 0; i < bit_length; i++) {
        char oxygen_bit = calculate_oxygen_bit(oxygen, i);
        std::erase_if(oxygen,
                      [&](std::string& str) { return str[i] != oxygen_bit; });

        if (co2.size() > 1) {
            char co2_bit = calculate_co2_bit(co2, i);
            std::erase_if(co2,
                          [&](std::string& str) { return str[i] != co2_bit; });
        }
    }

    print(oxygen);
    print(co2);

    long oxygen_value = std::bitset<12>(oxygen[0]).to_ulong();
    long co2_value    = std::bitset<12>(co2[0]).to_ulong();

    return oxygen_value * co2_value;
}

int main(int argc, char* argv[]) {
    std::ifstream            file(uri);
    std::string              number;
    std::vector<std::string> numbers;

    while (file.is_open() && file >> number) {
        numbers.push_back(number);
    }

    std::cout << "Result = " << proceed(numbers) << std::endl;
}