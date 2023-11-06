import re


class RfcActions:
    @classmethod
    def validate_rfc(cls, archive_path: str) -> dict:
        selected_archive = RfcActions.read_archive(archive_path)
        matches = RfcActions.filter_values(selected_archive)
        prev_rfc = None
        result = {}

        for match in matches:
            rfc, status = match.groups()
            if rfc:
                prev_rfc = rfc
            elif status == 'n' and prev_rfc:
                result[prev_rfc] = 'n'
            elif status == 'v' and prev_rfc:
                result[prev_rfc] = 'v'
        return result

    @classmethod
    def read_archive(cls, archive_path: str) -> str:
        with open(f"{archive_path}.txt", "r") as file:
            return file.read()

    @classmethod
    def filter_values(cls, selected_archive: str) -> iter:
        pattern = r'\b([A-Z]{4}\d{6}[A-Z0-9]{3})\b|(?<=RFC\s)([nv])'
        return re.finditer(pattern, selected_archive)
