"""模板方法模式 (Template Method)

意图：在父类中定义算法骨架，将某些步骤延迟到子类实现。
适用：数据导出、游戏回合流程、构建流程固定但细节可变。
"""

from abc import ABC, abstractmethod


class DataExporter(ABC):
    def export(self, rows: list[dict]) -> str:
        header = self.build_header()
        body = self.build_body(rows)
        footer = self.build_footer()
        return f"{header}\n{body}\n{footer}"

    @abstractmethod
    def build_header(self) -> str:
        pass

    @abstractmethod
    def build_body(self, rows: list[dict]) -> str:
        pass

    def build_footer(self) -> str:
        return "--- END ---"


class CsvExporter(DataExporter):
    def build_header(self) -> str:
        return "name,amount"

    def build_body(self, rows: list[dict]) -> str:
        return "\n".join(f"{r['name']},{r['amount']}" for r in rows)


class JsonExporter(DataExporter):
    def build_header(self) -> str:
        return "["

    def build_body(self, rows: list[dict]) -> str:
        import json
        return ",\n".join(json.dumps(r, ensure_ascii=False) for r in rows)

    def build_footer(self) -> str:
        return "]"


def demo() -> None:
    rows = [{"name": "Alice", "amount": 100}, {"name": "Bob", "amount": 200}]
    for exporter in [CsvExporter(), JsonExporter()]:
        print(f"[TemplateMethod] {exporter.__class__.__name__}:\n{exporter.export(rows)}\n")


if __name__ == "__main__":
    demo()
