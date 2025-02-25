
import sys
def print_door_mat(N, M):
    pattern = [('.|.' * (2 * i + 1)).center(M, '-') for i in range(N//2)]
    print('\n'.join(pattern + ['WELCOME'.center(M, '-')] + pattern[::-1]))
    
if __name__ == '__main__':
    N, M = map(int, sys.stdin.read().split())
    print_door_mat(N, M)
    
# Su dung STDIN nen khi ket thuc output va muon xuat ra output thì an Ctrl + Z > Enter de gui message EOL cho STIN