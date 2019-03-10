"""ログ出力クラス."""

import logging


class Logger:
    """Log出力クラス。"""

    logger = None
    available_log_levels = {'NOTEST': 0, 'DEBUG': 10, 'INFO': 20,
                            'WARNING': 30, 'ERROR': 40, 'CRITICAL': 50}

    def __init__(self, file_path: str, log_levl_string: str = 'DEBUG'):
        self.file_path = file_path
        self.log_level = self._get_log_level_number(log_levl_string)
        self.log_name = 'logger'
        self._set_logger()

    def _set_logger(self):
        self.logger = logging.getLogger(self.log_name)
        self.logger.setLevel(self.log_level)
        fh = logging.FileHandler(self.file_path)
        self.logger.addHandler(fh)
        sh = logging.StreamHandler()
        self.logger.addHandler(sh)
        formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
        fh.setFormatter(formatter)
        sh.setFormatter(formatter)

    def set_log_level(self, log_level_string: str):
        self.log_level = self._get_log_level_number(log_level_string)
        self.logger.setLevel(self.log_level)

    def _is_valid_log_level_string(self, log_level_string: str) -> bool:
        for keys in self.available_log_levels.keys():
            if log_level_string == keys:
                return True
        return False

    def _get_log_level_number(self, log_level_string: str) -> int:
        if not self._is_valid_log_level_string(log_level_string):
            message = f'loglevel:[{log_level_string}] is not available, '
            available = ','.join(self.available_log_levels.keys())
            message += f'available:{available}'
            raise ValueError(message)
        return self.available_log_levels[log_level_string]

    def log(self, log_level_string: str, message: str):
        """ログを出力する。"""
        log_level_number = self._get_log_level_number(log_level_string)
        self.logger.log(log_level_number, message)

    def get_available_log_levels(self) -> list:
        """ログレベルを列挙する。"""
        return self.available_log_levels.keys()

    def notest(self, message: str) -> None:
        self.log('NOTEST', message)

    def debug(self, message: str) -> None:
        self.log('DEBUG', message)

    def info(self, message: str) -> None:
        self.log('INFO', message)

    def warning(self, message: str) -> None:
        self.log('WARNING', message)

    def error(self, message: str) -> None:
        self.log('ERROR', message)

    def critical(self, message: str) -> None:
        self.log('CRITICAL', message)

    def close(self) -> None:
        logging.shutdown()
