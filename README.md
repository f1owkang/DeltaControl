# Delta_Control — Delta 机器人运动学反解 (Delta Robot Inverse Kinematics)

> [!WARNING]
> **本项目已归档 (Archived) · 不再维护 (No longer maintained)**
> 最后更新于 2023-07,仓库内容已封存,仅供检索与参考。

## 简介 / Introduction

Delta 并联机器人的逆运动学求解(Delta robot inverse kinematics):给定动平台中心坐标 `(x, y, z)`,计算三个主动臂转角 `θ1 θ2 θ3`(单位:弧度)。

原理:对每条运动链建立约束方程,整理为关于 `t = tan(θ/2)` 的一元二次方程 `A·t² + B·t + C = 0`,取负根得解。三种实现算法一致,仅语言与几何参数不同。

## 实现 / Implementations

| 文件 | 语言 | R | r | L | l | 备注 |
|---|---|---|---|---|---|---|
| [`Delta_Control.py`](Delta_Control.py) | Python | 50 | 20 | 275 | 500 | 已实测验证 |
| [`Delta_Control.ino`](Delta_Control.ino) | Arduino C++ | 100 | 20 | 270 | 500 | — |
| [`Delta_Control.m`](Delta_Control.m) | MATLAB | 90 | 41.57 | 85 | 140 | — |

三份实现对应不同尺寸的机构,使用前请按自己的机器人修改对应文件顶部的几何参数。

## 参数说明 / Parameters

| 符号 | 含义 |
|---|---|
| `R` | 动平台半径(关节轴到中心) |
| `r` | 静平台半径 |
| `L` | 主动臂臂长 |
| `l` | 从动臂臂长 |

坐标系约定:原点位于静平台中心;代码内部执行 `z = -z`,传入的 `z` 以向上为正。

## 快速上手 / Quick Start

**Python**

```bash
python Delta_Control.py
```

或作为模块调用:

```python
from Delta_Control import delta_inverse_kinematic

theta1, theta2, theta3 = delta_inverse_kinematic(x, y, z)
```

**Arduino**

将 [`Delta_Control.ino`](Delta_Control.ino) 中的 `delta_inverse_kinematic()` 函数拷贝进你的 sketch 直接调用。

**MATLAB**

```matlab
[theta1, theta2, theta3] = DeltaInversekinematic(x, y, z)
```

## License

[Apache-2.0](LICENSE)
