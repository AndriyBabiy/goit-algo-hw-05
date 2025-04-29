import timeit

class SearchAlgorithms:
    def boyer_moore(self, main_string, pattern):
        shift_table = self.build_shift_table(pattern)
        i = 0

        while i <= len(main_string) - len(pattern):
            j = len(pattern) - 1

            while j >= 0 and main_string[i + j] == pattern[j]:
                j -= 1

            if j < 0:
                return i

            i += shift_table.get(main_string[i + len(pattern) - 1], len(pattern))

        return -1

    def build_shift_table(self, pattern):
        table = {}
        length = len(pattern)

        for index, char in enumerate(pattern[:-1]):
            table[char] = length - index - 1

        table.setdefault(pattern[-1], length)
        return table

    def knuth_morris_pratt(self, main_string, pattern):
        M = len(pattern)
        N = len(main_string)

        lps = self.compute_lps(pattern)
        i = j = 0

        while i < N:
            if pattern[j] == main_string[i]:
                i += 1
                j += 1
            elif j != 0:
                j = lps[j - 1]
            else:
                i += 1

            if j == M:
                return i-j

        return -1

    def compute_lps(self, pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1

        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        return lps

    def rabin_karp(self, main_string, pattern):
        pattern_length = len(pattern)
        main_string_length = len(main_string)

        base = 256
        modulus = 101

        pattern_hash = self.polynomial_hash(pattern, base, modulus)
        current_slice_hash = self.polynomial_hash(main_string[:pattern_length], base, modulus)

        h_multiplier = pow(base, pattern_length - 1) % modulus

        for i in range(main_string_length - pattern_length + 1):
            if pattern_hash == current_slice_hash:
                if main_string[i:i+pattern_length] == pattern:
                    return i

            if i < main_string_length - pattern_length:
                current_slice_hash = (
                    (current_slice_hash - ord(main_string[i]) * h_multiplier)
                    * base + ord(main_string[i + pattern_length])
                ) % modulus

                if current_slice_hash < 0:
                    current_slice_hash += modulus

        return -1

    def polynomial_hash(self, s, base=256, modulus=101):
        n = len(s)
        hash_value = 0
        for i, char in enumerate(s):
            power_of_base = pow(base, n - i - 1) % modulus
            hash_value = (hash_value + ord(char) * power_of_base) % modulus
        return hash_value

def timed(func):
    return timeit.timeit(f"{func}", setup="from __main__ import file_content, pattern, SearchAlgorithms")

if __name__ == "__main__":
    files = ('./стаття_1.txt', './стаття_2.txt')

    pattern = ("Література", "Літератураа", "Автори публiкації", "https://dou.ua/", "AMD Ryzen 5 3600")

    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            file_content = f.read()

        print()
        print(f"| {(file) :<112} |")
        print(f"| {'-' * 112} |")
        print(f"| {'Word' :<20} | {'Location' :<20} | {'KnuthMorrisPratt' :<20} | {'RabinKarp' :<20} | {'BoyerMoore' :<20} |")
        print(f"| {'-'*20} | {'-'*20} | {'-'*20} | {'-'*20} | {'-'*20} |")

        for el in pattern:
            location = SearchAlgorithms().knuth_morris_pratt(file_content, el)
            kmp = timed(SearchAlgorithms().knuth_morris_pratt(file_content, el))
            rk = timed(SearchAlgorithms().rabin_karp(file_content, el))
            bm = timed(SearchAlgorithms().boyer_moore(file_content, el))

            print(f"| {el :<20} | {location :<20} | {round(kmp, 7) :<20} | {round(rk, 7) :<20} | {round(bm, 7) :<20} |")
