import streamlit as st
from py_mod import line_print, st_print, st_code

### StartofFunc###


def py_P28():
    import os

    def readme():
        try:
            with open("py10_algorithms/flashield_P28.txt", "r") as f:
                readme = f.read()
                st_print(readme)
        except Exception as e:
            st_print(f"Error reading README file: {str(e)}")
        finally:
            pass

    def max_suffix(pattern, inverse_order=False):
        """
        Computes the maximal suffix of the pattern lexicographically.
        Returns a tuple of (cut_index, period).
        """
        n = len(pattern)
        i = -1
        j = 0
        k = 1
        p = 1

        while j + k < n:
            a = pattern[i + k]
            b = pattern[j + k]

            # Invert the comparison based on the alphabet ordering
            if inverse_order:
                is_less = a > b
                is_greater = a < b
            else:
                is_less = a < b
                is_greater = a > b

            if is_less:
                j += k
                k = 1
                p = j - i
            elif a == b:
                if k == p:
                    j += p
                    k = 1
                else:
                    k += 1
            elif is_greater:
                i = j
                j = i + 1
                k = 1
                p = 1

            if is_less:
                j += k
                k = 1
                p = j - i
            elif a == b:
                if k == p:
                    j += p
                    k = 1
                else:
                    k += 1
            elif is_greater:
                j = i + 1
                k = 1
                p = 1

        return j, p

    def critical_factorization(pattern):
        """
        Finds a critical factorization point (cut) where the period of the 
        pattern can be realized local to the split.
        """
        cut1, period1 = max_suffix(pattern, inverse_order=False)
        cut2, period2 = max_suffix(pattern, inverse_order=True)

        if cut1 > cut2:
            return cut1, period1
        else:
            return cut2, period2

        if cut1 > cut2:
            return cut1, period1
        else:
            return cut2, period2

    def two_way_search(text, pattern):
        """
        Searches for all occurrences of 'pattern' in 'text' 
        using the Crochemore-Perrin Two-Way Algorithm.
        Returns a list of starting indices.
        """
        n = len(text)
        m = len(pattern)

        if m == 0:
            return [0]
        if n < m:
            return []

        # Preprocessing Phase
        cut, period = critical_factorization(pattern)

        # Check if the prefix is periodic
        is_periodic = pattern[0:cut] == pattern[period:cut + period]

        matches = []
        i = 0  # Position window in text

        if is_periodic:
            memory = 0
            while i <= n - m:
                # 1. Match the right part of the pattern
                j = max(cut, memory)
                while j < m and pattern[j] == text[i + j]:
                    j += 1

                if j < m:
                    # Mismatch on the right side
                    i += (j - cut + 1)
                    memory = 0
                else:
                    # 2. Match the left part of the pattern
                    j = cut - 1
                    while j >= memory and pattern[j] == text[i + j]:
                        j -= 1

                    if j < memory:
                        matches.append(i)

                    i += period
                    memory = m - period
        else:
            while i <= n - m:
                # 1. Match the right part of the pattern
                j = cut
                while j < m and pattern[j] == text[i + j]:
                    j += 1

                if j < m:
                    # Mismatch on the right side
                    i += (j - cut + 1)
                else:
                    # 2. Match the left part of the pattern
                    j = cut - 1
                    while j >= 0 and pattern[j] == text[i + j]:
                        j -= 1

                    if j < 0:
                        matches.append(i)

                    # Safe shift based on the cut location
                    i += max(cut + 1, m - cut)

        return matches
    readme()
    haystack = "GCATCGCAGAGAGTATACAGTACG"
    needle = "GCAGAGAG"

    results = two_way_search(haystack, needle)
    st_code(f"Pattern found at indices: {results}")
### EndofCodeSection###
