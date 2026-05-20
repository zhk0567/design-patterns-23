# 23 种设计模式关系总图

便于把握模式分类、易混淆对与典型组合。

## 分类一览

```mermaid
flowchart TB
  subgraph creational [创建型 Creational]
    S01[01 Singleton]
    S02[02 Factory Method]
    S03[03 Abstract Factory]
    S04[04 Builder]
    S05[05 Prototype]
  end
  subgraph structural [结构型 Structural]
    S06[06 Adapter]
    S07[07 Bridge]
    S08[08 Composite]
    S09[09 Decorator]
    S10[10 Facade]
    S11[11 Flyweight]
    S12[12 Proxy]
  end
  subgraph behavioral [行为型 Behavioral]
    S13[13 Chain]
    S14[14 Command]
    S15[15 Interpreter]
    S16[16 Iterator]
    S17[17 Mediator]
    S18[18 Memento]
    S19[19 Observer]
    S20[20 State]
    S21[21 Strategy]
    S22[22 Template Method]
    S23[23 Visitor]
  end
```

## 易混淆模式对

```mermaid
flowchart LR
  FM[02 Factory Method] -.->|一种产品| AF[03 Abstract Factory]
  ST[20 State] -.->|内部驱动切换| SG[21 Strategy]
  AD[06 Adapter] -.->|改接口| DC[09 Decorator]
  DC -.->|增强同接口| PX[12 Proxy]
  BR[07 Bridge] -.->|抽象与实现分离| SG
  FM2[10 Facade] -.->|简化入口| MD[17 Mediator]
  OB[19 Observer] -.->|广播| MD
  CM[14 Command] -.->|封装请求| MM[18 Memento]
```

## 电商场景常用组合

```mermaid
flowchart LR
  User[用户下单] --> Facade[10 Facade]
  Facade --> State[20 State]
  State --> Observer[19 Observer]
  Facade --> Chain[13 Chain 大额审批]
  Command[14 Command 取消/改址] --> State
```

运行端到端演示：`python scripts/ecommerce_demo.py`

## 速查

| 若你需要… | 优先考虑 |
|-----------|----------|
| 全局唯一配置 | Singleton |
| 一族产品一起换 | Abstract Factory |
| 分步构建复杂对象 | Builder |
| 旧接口对接 | Adapter |
| 动态叠加能力 | Decorator |
| 简化多子系统调用 | Facade |
| 状态驱动行为变化 | State |
| 算法可替换 | Strategy |
| 一对多通知 | Observer |
| 撤销操作 | Command |

详见 [PATTERNS_COMPARE.md](PATTERNS_COMPARE.md)、[ECOMMERCE_SCENARIO.md](ECOMMERCE_SCENARIO.md)。
