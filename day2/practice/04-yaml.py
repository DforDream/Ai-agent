from pathlib import Path
import yaml

yaml_path = Path("project/docs/test.yaml")
content = yaml_path.read_text(encoding="utf-8")
data = yaml.safe_load(content)
data['app']['version'] = "1.0.1"
yaml_path.write_text(
    yaml.safe_dump(data, sort_keys=False, allow_unicode=True),
    encoding="utf-8"
)