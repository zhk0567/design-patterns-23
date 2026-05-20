# 设计模式与主流框架对照

说明：框架往往**组合多种模式**，下表为常见对应关系，便于从「课本示例」过渡到工程阅读。

## Spring（Java）

| 模式 | Spring 中的体现 | 备注 |
|------|-----------------|------|
| Singleton | 默认 Bean 作用域 `singleton` | `@Component` 容器管理 |
| Factory Method | `FactoryBean` | 由工厂决定 Bean 类型 |
| Abstract Factory | `BeanFactory` / 多 `ApplicationContext` | 一族 Bean 配置 |
| Builder | `RestTemplateBuilder`、`UriComponentsBuilder` | 流式组装 |
| Prototype | `@Scope("prototype")` | 每次注入新实例 |
| Adapter | `HandlerAdapter`、各种 `*Adapter` | MVC 适配不同 Controller |
| Proxy | AOP、`JdkDynamicProxy` | 事务、日志切面 |
| Decorator | `HttpServletRequestWrapper` | 包装请求增强 |
| Facade | `@Service` 编排多个 `@Repository` | 业务门面 |
| Template Method | `JdbcTemplate`、`JmsTemplate` | 固定骨架，子类/回调填细节 |
| Strategy | `PaymentStrategy` 等业务接口多实现 | 常配合 `@Qualifier` |
| Observer | `ApplicationEvent` / `@EventListener` | 事件驱动 |
| Chain of Responsibility | `FilterChain`、Security 过滤器链 | Servlet Filter |
| Command | 部分 CQRS / 任务队列封装 | 非单一 API |
| State | 工作流引擎（Flowable 等）集成 | 或手写状态机 |
| Visitor | 较少直接用 | AST/编译器场景更多 |

## Django（Python）

| 模式 | Django 中的体现 | 备注 |
|------|-----------------|------|
| Singleton | `settings`、数据库连接 | 模块级单例惯例 |
| Factory Method | `Model.objects.create` 等 Manager 方法 | 可自定义 Manager |
| Template Method | 类视图 `View.dispatch` → `get/post` | 固定请求处理流程 |
| Iterator | `QuerySet.__iter__` | 惰性查询迭代 |
| Observer | Signals：`post_save`、`pre_delete` | `receiver` 订阅 |
| Facade | 高层 API 如 `django.contrib.auth.login` | 隐藏多步细节 |
| Proxy | `LazyObject`、`SimpleLazyObject` | 延迟加载 |
| Decorator | 中间件 `Middleware`、视图 `@login_required` | 请求/函数包装 |
| Adapter | 序列化 `Serializer`、第三方认证 Backend | 接口转换 |
| Strategy | 认证/缓存/存储 Backend 可插拔 | `AUTHENTICATION_BACKENDS` |
| Composite | `Model` 继承、`MPTT` 树形模型 | 统一接口处理节点 |
| Memento | 无内置 | `django-reversion` 等第三方 |
| Mediator | 较少直接用 | Signals 有部分中介效果 |

## 与本仓库示例的对照

| 本仓库文件 | 框架阅读时可联想 |
|------------|------------------|
| `10_facade.py` | Spring `@Service` 下单编排 |
| `19_observer.py` | Django Signals / Spring Events |
| `20_state.py` | 订单状态字段 + 转移校验 |
| `12_proxy.py` | Spring AOP 懒加载代理 |
| `21_strategy.py` | 运费/支付 Strategy 接口多实现 |

## 延伸阅读

- [PATTERNS_COMPARE.md](PATTERNS_COMPARE.md) — 模式之间区别
- [STDLIB_MAPPING.md](STDLIB_MAPPING.md) — Python 标准库对照
- [ECOMMERCE_SCENARIO.md](ECOMMERCE_SCENARIO.md) — 统一业务场景
