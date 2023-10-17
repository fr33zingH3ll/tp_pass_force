class IntegerOptions:
    """
    Options for integer fields in a database table.

    Options:
        - integer: Default integer field option.
        - integer_pk: Integer field option with primary key constraint.
        - integer_ai: Integer field option with primary key and auto-increment constraint.
        - smallint: Small integer field option.
        - bigint: Big integer field option.
        - Add more options as needed.

    Example:
        integer_option = IntegerOptions.integer  # Get the value for 'INTEGER'
        integer_pk_option = IntegerOptions.integer_pk  # Get the value for 'INTEGER PRIMARY KEY'
        integer_ai_option = IntegerOptions.integer_ai  # Get the value for 'INTEGER PRIMARY KEY AUTOINCREMENT'
    """

    integer = 'INTEGER'
    integer_pk = 'INTEGER PRIMARY KEY'
    integer_ai = 'INTEGER PRIMARY KEY AUTOINCREMENT'
    smallint = 'SMALLINT'
    bigint = 'BIGINT'
    # Add more options as needed


class RealOptions:
    """
    Options for real number fields in a database table.

    Options:
        - real: Default real field option.
        - real_pk: Real field option with primary key constraint.
        - real_ai: Real field option with primary key and auto-increment constraint.
        - double: Double precision floating-point field option.
        - Add more options as needed.

    Example:
        real_option = RealOptions.real  # Get the value for 'REAL'
        real_pk_option = RealOptions.real_pk  # Get the value for 'REAL PRIMARY KEY'
        real_ai_option = RealOptions.real_ai  # Get the value for 'REAL PRIMARY KEY AUTOINCREMENT'
    """

    real = 'REAL'
    real_pk = 'REAL PRIMARY KEY'
    real_ai = 'REAL PRIMARY KEY AUTOINCREMENT'
    double = 'DOUBLE'
    # Add more options as needed


class TextOptions:
    """
    Options for text fields in a database table.

    Options:
        - text: Default text field option.
        - text_pk: Text field option with primary key constraint.
        - text_ai: Text field option with primary key and auto-increment constraint.
        - varchar: Variable-length text field option.
        - Add more options as needed.

    Example:
        text_option = TextOptions.text  # Get the value for 'TEXT'
        text_pk_option = TextOptions.text_pk  # Get the value for 'TEXT PRIMARY KEY'
        text_ai_option = TextOptions.text_ai  # Get the value for 'TEXT PRIMARY KEY AUTOINCREMENT'
    """

    text = 'TEXT'
    text_pk = 'TEXT PRIMARY KEY'
    text_ai = 'TEXT PRIMARY KEY AUTOINCREMENT'
    varchar = 'VARCHAR'
    # Add more options as needed


class BlobOptions:
    """
    Options for binary data (BLOB) fields in a database table.

    Options:
        - blob: Default BLOB field option.
        - Add more options as needed.

    Example:
        blob_option = BlobOptions.blob  # Get the value for 'BLOB'
    """

    blob = 'BLOB'
    # Add more options as needed
