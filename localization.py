import json
import os
from typing import Dict, Any, Optional

class Localization:
    def __init__(self, locale_dir: str = "locale", default_locale: str = "en"):
        self.locale_dir = locale_dir
        self.default_locale = default_locale
        self.translations: Dict[str, Dict[str, Any]] = {}
        self.current_locale = default_locale

    def load_translations(self):
        """加载所有语言文件"""
        if not os.path.exists(self.locale_dir):
            raise FileNotFoundError(f"Locale directory '{self.locale_dir}' not found")

        for filename in os.listdir(self.locale_dir):
            if filename.endswith(".json"):
                lang_code = filename[:-5]  # 去掉 .json 扩展名
                file_path = os.path.join(self.locale_dir, filename)
                with open(file_path, "r", encoding="utf-8") as f:
                    self.translations[lang_code] = json.load(f)

    def set_locale(self, locale: str):
        """设置当前语言"""
        if locale not in self.translations:
            if locale != self.default_locale:
                print(f"Warning: Locale '{locale}' not found, using default '{self.default_locale}'")
                locale = self.default_locale
        self.current_locale = locale

    def get_translation(self, key: str, default: Optional[str] = None) -> str:
        """
        获取翻译值
        支持多层键，例如 "greeting.hello" 或 "error.not_found"
        """
        parts = key.split(".")
        current = self.translations.get(self.current_locale, {})

        for part in parts:
            if part in current:
                current = current[part]
            else:
                # 如果找不到，尝试使用默认语言
                default_translation = self.translations.get(self.default_locale, {})
                current_default = default_translation
                for part in parts:
                    if part in current_default:
                        current_default = current_default[part]
                    else:
                        current_default = None
                        break
                if current_default is not None:
                    return str(current_default)
                # 如果仍然找不到，返回默认值或空字符串
                return default or ""

        return str(current)

# 创建一个单例实例
_ = Localization()
_.load_translations()
