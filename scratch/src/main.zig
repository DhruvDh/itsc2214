const std = @import("std");

const nums = packed struct {
    a: u2, // 4bit
    b: u2 // 4bit
};

pub fn main() void {
    printSize(nums);
}

fn printSize(comptime strct: type) void {
    std.debug.warn("Size of \"{}\" struct: {} bits\n", .{
        @typeName(strct),
        @bitSizeOf(strct)
    });
}