# SPDX-FileCopyrightText: © 2026 Joe T. Sylve, Ph.D. <joe.sylve@gmail.com>
#
# SPDX-License-Identifier: MIT OR Apache-2.0

"""Ghidra-specific tool visibility constants."""

from re_mcp.transforms import MANAGEMENT_TOOLS, META_TOOLS

PINNED_TOOLS = frozenset(
    {
        *MANAGEMENT_TOOLS,
        *META_TOOLS,
        # Exploration
        "get_database_info",
        "list_functions",
        "get_strings",
        "decompile_function",
        "disassemble_function",
        "list_names",
        "find_code_by_string",
        "get_xrefs_to",
        "get_xrefs_from",
        "get_call_graph",  # THTK fork: subsystem mapping (player main loop, bullet/ECL call trees)
        "read_bytes",  # THTK fork: read program memory (constants/tables/key bytes) — replaces ad-hoc PE parsing
        # Mutation
        "rename_function",
        "rename_address",  # THTK fork: pin data/label rename (DAT_xxxx globals) so it shows in client tool lists
        "list_decompiler_variables",  # THTK fork: list a function's locals/params before rename/retype
        "rename_decompiler_variable",  # THTK fork: pin decompiler local/param rename
        "retype_decompiler_variable",  # THTK fork: pin decompiler local/param retype
        "set_comment",
        "set_decompiler_comment",
        # Function signatures (THTK fork: VM handler / thiscall prototype fixes -> readable decompile)
        "set_function_type",
        "set_function_calling_convention",
        # Structs
        "list_structures",
        "get_structure",
        "create_structure",
        "add_struct_member",
        "retype_struct_member",
        # Types
        "list_local_types",
        "parse_type_declaration",
        "apply_type_at_address",
        "get_type_info",
        "set_type",
    }
)
