"""Validate the YAML issue template structurally."""
import yaml, sys

with open("/tmp/repo_intro_si/.github/ISSUE_TEMPLATE/historia_de_usuario.yml") as f:
    template = yaml.safe_load(f)

errors = []
required_top = ["name", "description", "body"]
for k in required_top:
    if k not in template:
        errors.append(f"MISSING top-level: {k}")

if "body" in template:
    seen_ids = set()
    for i, section in enumerate(template["body"]):
        t = section.get("type")
        sid = section.get("id", f"<no id at index {i}>")
        attrs = section.get("attributes", {})
        if not t:
            errors.append(f"body[{i}] ({sid}): MISSING type")
            continue
        if sid in seen_ids:
            errors.append(f"body[{i}] ({sid}): DUPLICATE id")
        seen_ids.add(sid)
        if t in ("input", "textarea", "dropdown", "checkboxes", "upload"):
            if "label" not in attrs:
                errors.append(f"body[{i}] ({sid}) type={t}: MISSING label")
        if t in ("dropdown", "checkboxes"):
            if "options" not in attrs:
                errors.append(f"body[{i}] ({sid}) type={t}: MISSING options in attributes")
            elif not isinstance(attrs["options"], list) or len(attrs["options"]) == 0:
                errors.append(f"body[{i}] ({sid}) type={t}: options must be a non-empty list")
        if t == "markdown":
            if "value" not in attrs:
                errors.append(f"body[{i}] ({sid}) type=markdown: MISSING value in attributes")
        if "validations" in section:
            v = section["validations"]
            if "required" in v and not isinstance(v["required"], bool):
                errors.append(f"body[{i}] ({sid}): validations.required must be bool")

if errors:
    print("❌ ERRORS:")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)
else:
    print(f"✓ Template válido")
    print(f"  Nombre: {template['name']}")
    print(f"  Descripción: {template['description']}")
    print(f"  Labels: {template.get('labels', [])}")
    print(f"  Title prefix: {template.get('title', '(none)')}")
    print(f"  Body: {len(template['body'])} secciones")
    for i, s in enumerate(template["body"]):
        sid = s.get("id", "?")
        t = s.get("type", "?")
        label = s.get("attributes", {}).get("label", "?")
        req = s.get("validations", {}).get("required", False)
        print(f"    [{i}] {t:<12} id={sid:<25} label='{label}' required={req}")
