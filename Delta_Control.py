import math


def delta_inverse_kinematic(x, y, z):
    # Delta反解 已经实践测量
    # 动平台半径（轴到中心）
    R = 50
    # 静平台半径
    r = 20
    # 主动臂臂长
    L = 275
    # 从动臂臂长
    l = 500

    z = -z
    m = x**2 + y**2 + z**2 + (R - r)**2 + L**2 - l**2
    A = [
        (m - 2*x*(R - r))/(2*L) - (R - r - x),
        (m + (R - r)*(x - math.sqrt(3)*y))/(L) - 2*(R - r) - (x - math.sqrt(3)*y),
        (m + (R - r)*(x + math.sqrt(3)*y))/(L) - 2*(R - r) - (x + math.sqrt(3)*y)
    ]
    B = [
        2*z,
        4*z,
        4*z
    ]
    C = [
        (m - 2*x*(R - r))/(2*L) + (R - r - x),
        (m + (R - r)*(x - math.sqrt(3)*y))/(L) + 2*(R - r) + (x - math.sqrt(3)*y),
        (m + (R - r)*(x + math.sqrt(3)*y))/(L) + 2*(R - r) + (x + math.sqrt(3)*y)
    ]
    theta1 = 2*math.atan((-B[0] - math.sqrt(B[0]**2 - 4*A[0]*C[0]))/(2*A[0]))
    theta2 = 2*math.atan((-B[1] - math.sqrt(B[1]**2 - 4*A[1]*C[1]))/(2*A[1]))
    theta3 = 2*math.atan((-B[2] - math.sqrt(B[2]**2 - 4*A[2]*C[2]))/(2*A[2]))
    return theta1, theta2, theta3


def degrees(rad):
    return rad * 180 / math.pi


if __name__ == "__main__":
    # 测试数据
    test_cases = [
        (0, 0, 765)
    ]

    for x, y, z in test_cases:
        theta1, theta2, theta3 = delta_inverse_kinematic(x, y, z)
        # 转换为度数
        theta1_deg = degrees(theta1)
        theta2_deg = degrees(theta2)
        theta3_deg = degrees(theta3)
        print(f"Input: ({x}, {y}, {z})")
        print(f"Output: theta1={theta1_deg}°, theta2={theta2_deg}°, theta3={theta3_deg}°")
        print("------------------------------")
