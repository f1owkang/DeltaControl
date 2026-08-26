<div align="center">

# 🤖 DeltaControl

**Delta 并联机器人逆运动学求解：给定动平台中心坐标 `(x, y, z)`，解出三个主动臂转角 `θ1 θ2 θ3`**

[![Release](https://img.shields.io/github/v/release/f1owkang/DeltaControl?style=flat-square&label=Release&color=blue)](https://github.com/f1owkang/DeltaControl/releases)
[![Downloads](https://img.shields.io/github/downloads/f1owkang/DeltaControl/total?style=flat-square&label=Downloads&color=green)](https://github.com/f1owkang/DeltaControl/releases)
[![Language](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org)
[![Platform](https://img.shields.io/badge/Platform-Windows_%7C_Linux_%7C_macOS_%7C_Arduino-blue?style=flat-square)](#快速上手)
[![License](https://img.shields.io/github/license/f1owkang/DeltaControl?style=flat-square&label=License&color=orange)](LICENSE)

[简介](#简介) · [原理](#原理) · [实现](#实现) · [参数说明](#参数说明) · [快速上手](#快速上手)

</div>

---

> [!WARNING]
> **本项目已归档 (Archived)，不再维护。** 最后更新于 2023-07，仓库已封存，仅供检索与参考。

## 简介

给定 Delta 并联机器人动平台中心坐标 `(x, y, z)`，逆运动学求解三个主动臂转角 `θ1 θ2 θ3`（单位：弧度）。

## 原理

对每条运动链建立约束方程，整理为关于 `t = tan(θ/2)` 的一元二次方程 `A·t² + B·t + C = 0`，取负根即得解。三种实现算法完全一致，仅语言与几何参数不同。

## 实现

| 文件 | 语言 | R | r | L | l | 备注 |
| :-- | :-- | :--: | :--: | :--: | :--: | :-- |
| [`Delta_Control.py`](Delta_Control.py) | Python | 50 | 20 | 275 | 500 | 已实测验证 |
| [`Delta_Control.ino`](Delta_Control.ino) | Arduino C++ | 100 | 20 | 270 | 500 | — |
| [`Delta_Control.m`](Delta_Control.m) | MATLAB | 90 | 41.57 | 85 | 140 | — |

> [!NOTE]
> 三份实现对应不同尺寸的机构，使用前请先修改对应文件顶部的几何参数。

## 参数说明

| 符号 | 含义 |
| :--: | :-- |
| `R` | 动平台半径（关节轴到中心） |
| `r` | 静平台半径 |
| `L` | 主动臂臂长 |
| `l` | 从动臂臂长 |

坐标系约定：原点位于静平台中心；代码内部执行 `z = -z`，传入的 `z` 以向上为正。

## 快速上手

**Python**

```bash
python Delta_Control.py
```

或作为模块调用：

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

## 开源协议

本项目以 [Apache-2.0](LICENSE) 协议开源。

---

<div align="center">

**Made with ❤ by [f1owkang](https://github.com/f1owkang)**

</div>
