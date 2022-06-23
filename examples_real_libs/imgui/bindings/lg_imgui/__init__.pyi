# type: ignore
import sys
from typing import Literal, List, Any
import numpy as np
from enum import Enum
import numpy

##################################################
#    Manually inserted code (typedefs, etc.)
##################################################
class BoxedFloat:
    value: float

class BoxedInt:
    value: int

class BoxedBool:
    value: bool


VoidPtr = Any

#-----------------------------------------------------------------------------
# [SECTION] Forward declarations and basic types
#-----------------------------------------------------------------------------

"""
// Forward declarations
struct ImDrawChannel;               // Temporary storage to output draw commands out of order, used by ImDrawListSplitter and ImDrawList::ChannelsSplit()
struct ImDrawCmd;                   // A single draw command within a parent ImDrawList (generally maps to 1 GPU draw call, unless it is a callback)
struct ImDrawData;                  // All draw command lists required to render the frame + pos/size coordinates to use for the projection matrix.
struct ImDrawList;                  // A single draw command list (generally one per window, conceptually you may see this as a dynamic "mesh" builder)
struct ImDrawListSharedData;        // Data shared among multiple draw lists (typically owned by parent ImGui context, but you may create one yourself)
struct ImDrawListSplitter;          // Helper to split a draw list into different layers which can be drawn into out of order, then flattened back.
struct ImDrawVert;                  // A single vertex (pos + uv + col = 20 bytes by default. Override layout with IMGUI_OVERRIDE_DRAWVERT_STRUCT_LAYOUT)
struct ImFont;                      // Runtime data for a single font within a parent ImFontAtlas
struct ImFontAtlas;                 // Runtime data for multiple fonts, bake multiple fonts into a single texture, TTF/OTF font loader
struct ImFontBuilderIO;             // Opaque interface to a font builder (stb_truetype or FreeType).
struct ImFontConfig;                // Configuration data when adding a font or merging fonts
struct ImFontGlyph;                 // A single font glyph (code point + coordinates within in ImFontAtlas + offset)
struct ImFontGlyphRangesBuilder;    // Helper to build glyph ranges from text/string data
struct ImColor;                     // Helper functions to create a color that can be converted to either u32 or float4 (*OBSOLETE* please avoid using)
struct ImGuiContext;                // Dear ImGui context (opaque structure, unless including imgui_internal.h)
struct ImGuiIO;                     // Main configuration and I/O between your application and ImGui
struct ImGuiInputTextCallbackData;  // Shared state of InputText() when using custom ImGuiInputTextCallback (rare/advanced use)
struct ImGuiKeyData;                // Storage for ImGuiIO and IsKeyDown(), IsKeyPressed() etc functions.
struct ImGuiListClipper;            // Helper to manually clip large list of items
struct ImGuiOnceUponAFrame;         // Helper for running a block of code not more than once a frame
struct ImGuiPayload;                // User data payload for drag and drop operations
struct ImGuiPlatformImeData;        // Platform IME data for io.SetPlatformImeDataFn() function.
struct ImGuiSizeCallbackData;       // Callback data when using SetNextWindowSizeConstraints() (rare/advanced use)
struct ImGuiStorage;                // Helper for key->value storage
struct ImGuiStyle;                  // Runtime data for styling/colors
struct ImGuiTableSortSpecs;         // Sorting specifications for a table (often handling sort specs for a single column, occasionally more)
struct ImGuiTableColumnSortSpecs;   // Sorting specification for one column of a table
struct ImGuiTextBuffer;             // Helper to hold and append into a text buffer (~string builder)
struct ImGuiTextFilter;             // Helper to parse and apply text filters (e.g. "aaaaa[,bbbbb][,ccccc]")
struct ImGuiViewport;               // A Platform Window (always only one in 'master' branch), in the future may represent Platform Monitor
"""
# We forward declare only the opaque structures
ImGuiContext = Any
ImDrawListSharedData = Any
ImDrawVert = Any
ImFontBuilderIO = Any


"""
// Enums/Flags (declared as int for compatibility with old C++, to allow using as flags without overhead, and to not pollute the top of this file)
// - Tip: Use your programming IDE navigation facilities on the names in the _central column_ below to find the actual flags/enum lists!
//   In Visual Studio IDE: CTRL+comma ("Edit.GoToAll") can follow symbols in comments, whereas CTRL+F12 ("Edit.GoToImplementation") cannot.
//   With Visual Assist installed: ALT+G ("VAssistX.GoToImplementation") can also follow symbols in comments.
typedef int ImGuiCol;               // -> enum ImGuiCol_             // Enum: A color identifier for styling
typedef int ImGuiCond;              // -> enum ImGuiCond_            // Enum: A condition for many Set*() functions
typedef int ImGuiDataType;          // -> enum ImGuiDataType_        // Enum: A primary data type
typedef int ImGuiDir;               // -> enum ImGuiDir_             // Enum: A cardinal direction
typedef int ImGuiKey;               // -> enum ImGuiKey_             // Enum: A key identifier
typedef int ImGuiNavInput;          // -> enum ImGuiNavInput_        // Enum: An input identifier for navigation
typedef int ImGuiMouseButton;       // -> enum ImGuiMouseButton_     // Enum: A mouse button identifier (0=left, 1=right, 2=middle)
typedef int ImGuiMouseCursor;       // -> enum ImGuiMouseCursor_     // Enum: A mouse cursor identifier
typedef int ImGuiSortDirection;     // -> enum ImGuiSortDirection_   // Enum: A sorting direction (ascending or descending)
typedef int ImGuiStyleVar;          // -> enum ImGuiStyleVar_        // Enum: A variable identifier for styling
typedef int ImGuiTableBgTarget;     // -> enum ImGuiTableBgTarget_   // Enum: A color target for TableSetBgColor()
typedef int ImDrawFlags;            // -> enum ImDrawFlags_          // Flags: for ImDrawList functions
typedef int ImDrawListFlags;        // -> enum ImDrawListFlags_      // Flags: for ImDrawList instance
typedef int ImFontAtlasFlags;       // -> enum ImFontAtlasFlags_     // Flags: for ImFontAtlas build
typedef int ImGuiBackendFlags;      // -> enum ImGuiBackendFlags_    // Flags: for io.BackendFlags
typedef int ImGuiButtonFlags;       // -> enum ImGuiButtonFlags_     // Flags: for InvisibleButton()
typedef int ImGuiColorEditFlags;    // -> enum ImGuiColorEditFlags_  // Flags: for ColorEdit4(), ColorPicker4() etc.
typedef int ImGuiConfigFlags;       // -> enum ImGuiConfigFlags_     // Flags: for io.ConfigFlags
typedef int ImGuiComboFlags;        // -> enum ImGuiComboFlags_      // Flags: for BeginCombo()
typedef int ImGuiDragDropFlags;     // -> enum ImGuiDragDropFlags_   // Flags: for BeginDragDropSource(), AcceptDragDropPayload()
typedef int ImGuiFocusedFlags;      // -> enum ImGuiFocusedFlags_    // Flags: for IsWindowFocused()
typedef int ImGuiHoveredFlags;      // -> enum ImGuiHoveredFlags_    // Flags: for IsItemHovered(), IsWindowHovered() etc.
typedef int ImGuiInputTextFlags;    // -> enum ImGuiInputTextFlags_  // Flags: for InputText(), InputTextMultiline()
typedef int ImGuiModFlags;          // -> enum ImGuiModFlags_        // Flags: for io.KeyMods (Ctrl/Shift/Alt/Super)
typedef int ImGuiPopupFlags;        // -> enum ImGuiPopupFlags_      // Flags: for OpenPopup*(), BeginPopupContext*(), IsPopupOpen()
typedef int ImGuiSelectableFlags;   // -> enum ImGuiSelectableFlags_ // Flags: for Selectable()
typedef int ImGuiSliderFlags;       // -> enum ImGuiSliderFlags_     // Flags: for DragFloat(), DragInt(), SliderFloat(), SliderInt() etc.
typedef int ImGuiTabBarFlags;       // -> enum ImGuiTabBarFlags_     // Flags: for BeginTabBar()
typedef int ImGuiTabItemFlags;      // -> enum ImGuiTabItemFlags_    // Flags: for BeginTabItem()
typedef int ImGuiTableFlags;        // -> enum ImGuiTableFlags_      // Flags: For BeginTable()
typedef int ImGuiTableColumnFlags;  // -> enum ImGuiTableColumnFlags_// Flags: For TableSetupColumn()
typedef int ImGuiTableRowFlags;     // -> enum ImGuiTableRowFlags_   // Flags: For TableNextRow()
typedef int ImGuiTreeNodeFlags;     // -> enum ImGuiTreeNodeFlags_   // Flags: for TreeNode(), TreeNodeEx(), CollapsingHeader()
typedef int ImGuiViewportFlags;     // -> enum ImGuiViewportFlags_   // Flags: for ImGuiViewport
typedef int ImGuiWindowFlags;       // -> enum ImGuiWindowFlags_     // Flags: for Begin(), BeginChild()
"""
ImGuiCol = int               # -> enum ImGuiCol_             # Enum: A color identifier for styling
ImGuiCond = int              # -> enum ImGuiCond_            # Enum: A condition for many Set*() functions
ImGuiDataType = int          # -> enum ImGuiDataType_        # Enum: A primary data type
ImGuiDir = int               # -> enum ImGuiDir_             # Enum: A cardinal direction
ImGuiKey = int               # -> enum ImGuiKey_             # Enum: A key identifier
ImGuiNavInput = int          # -> enum ImGuiNavInput_        # Enum: An input identifier for navigation
ImGuiMouseButton = int       # -> enum ImGuiMouseButton_     # Enum: A mouse button identifier (0=left, 1=right, 2=middle)
ImGuiMouseCursor = int       # -> enum ImGuiMouseCursor_     # Enum: A mouse cursor identifier
ImGuiSortDirection = int     # -> enum ImGuiSortDirection_   # Enum: A sorting direction (ascending or descending)
ImGuiStyleVar = int          # -> enum ImGuiStyleVar_        # Enum: A variable identifier for styling
ImGuiTableBgTarget = int     # -> enum ImGuiTableBgTarget_   # Enum: A color target for TableSetBgColor()
ImDrawFlags = int            # -> enum ImDrawFlags_          # Flags: for ImDrawList functions
ImDrawListFlags = int        # -> enum ImDrawListFlags_      # Flags: for ImDrawList instance
ImFontAtlasFlags = int       # -> enum ImFontAtlasFlags_     # Flags: for ImFontAtlas build
ImGuiBackendFlags = int      # -> enum ImGuiBackendFlags_    # Flags: for io.BackendFlags
ImGuiButtonFlags = int       # -> enum ImGuiButtonFlags_     # Flags: for InvisibleButton()
ImGuiColorEditFlags = int    # -> enum ImGuiColorEditFlags_  # Flags: for ColorEdit4(), ColorPicker4() etc.
ImGuiConfigFlags = int       # -> enum ImGuiConfigFlags_     # Flags: for io.ConfigFlags
ImGuiComboFlags = int        # -> enum ImGuiComboFlags_      # Flags: for BeginCombo()
ImGuiDragDropFlags = int     # -> enum ImGuiDragDropFlags_   # Flags: for BeginDragDropSource(), AcceptDragDropPayload()
ImGuiFocusedFlags = int      # -> enum ImGuiFocusedFlags_    # Flags: for IsWindowFocused()
ImGuiHoveredFlags = int      # -> enum ImGuiHoveredFlags_    # Flags: for IsItemHovered(), IsWindowHovered() etc.
ImGuiInputTextFlags = int    # -> enum ImGuiInputTextFlags_  # Flags: for InputText(), InputTextMultiline()
ImGuiModFlags = int          # -> enum ImGuiModFlags_        # Flags: for io.KeyMods (Ctrl/Shift/Alt/Super)
ImGuiPopupFlags = int        # -> enum ImGuiPopupFlags_      # Flags: for OpenPopup*(), BeginPopupContext*(), IsPopupOpen()
ImGuiSelectableFlags = int   # -> enum ImGuiSelectableFlags_ # Flags: for Selectable()
ImGuiSliderFlags = int       # -> enum ImGuiSliderFlags_     # Flags: for DragFloat(), DragInt(), SliderFloat(), SliderInt() etc.
ImGuiTabBarFlags = int       # -> enum ImGuiTabBarFlags_     # Flags: for BeginTabBar()
ImGuiTabItemFlags = int      # -> enum ImGuiTabItemFlags_    # Flags: for BeginTabItem()
ImGuiTableFlags = int        # -> enum ImGuiTableFlags_      # Flags: For BeginTable()
ImGuiTableColumnFlags = int  # -> enum ImGuiTableColumnFlags_# Flags: For TableSetupColumn()
ImGuiTableRowFlags = int     # -> enum ImGuiTableRowFlags_   # Flags: For TableNextRow()
ImGuiTreeNodeFlags = int     # -> enum ImGuiTreeNodeFlags_   # Flags: for TreeNode(), TreeNodeEx(), CollapsingHeader()
ImGuiViewportFlags = int     # -> enum ImGuiViewportFlags_   # Flags: for ImGuiViewport
ImGuiWindowFlags = int       # -> enum ImGuiWindowFlags_     # Flags: for Begin(), BeginChild()


"""
// ImTexture: user data for renderer backend to identify a texture [Compile-time configurable type]
// - To use something else than an opaque void* pointer: override with e.g. '#define ImTextureID MyTextureType*' in your imconfig.h file.
// - This can be whatever to you want it to be! read the FAQ about ImTextureID for details.
#ifndef ImTextureID
typedef void* ImTextureID;          // Default: store a pointer or an integer fitting in a pointer (most renderer backends are ok with that)
#endif
"""
ImTextureID = VoidPtr

"""
// ImDrawIdx: vertex index. [Compile-time configurable type]
// - To use 16-bit indices + allow large meshes: backend need to set 'io.BackendFlags |= ImGuiBackendFlags_RendererHasVtxOffset' and handle ImDrawCmd::VtxOffset (recommended).
// - To use 32-bit indices: override with '#define ImDrawIdx unsigned int' in your imconfig.h file.
#ifndef ImDrawIdx
typedef unsigned short ImDrawIdx;   // Default: 16-bit (for maximum compatibility with renderer backends)
#endif
"""
ImDrawIdx = int


"""
// Scalar data types
typedef unsigned int        ImGuiID;// A unique ID used by widgets (typically the result of hashing a stack of string)
typedef signed char         ImS8;   // 8-bit signed integer
typedef unsigned char       ImU8;   // 8-bit unsigned integer
typedef signed short        ImS16;  // 16-bit signed integer
typedef unsigned short      ImU16;  // 16-bit unsigned integer
typedef signed int          ImS32;  // 32-bit signed integer == int
typedef unsigned int        ImU32;  // 32-bit unsigned integer (often used to store packed colors)
typedef signed   long long  ImS64;  // 64-bit signed integer
typedef unsigned long long  ImU64;  // 64-bit unsigned integer
"""
# Scalar data types
ImGuiID = int# A unique ID used by widgets (typically the result of hashing a stack of string)
ImS8 = int   # 8-bit integer
ImU8 = int   # 8-bit integer
ImS16 = int  # 16-bit integer
ImU16 = int  # 16-bit integer
ImS32 = int  # 32-bit integer == int
ImU32 = int  # 32-bit integer (often used to store packed colors)
ImS64 = int  # 64-bit integer
ImU64 = int  # 64-bit integer


"""
// Character types
// (we generally use UTF-8 encoded string in the API. This is storage specifically for a decoded character used for keyboard input and display)
typedef unsigned short ImWchar16;   // A single decoded U16 character/code point. We encode them as multi bytes UTF-8 when used in strings.
typedef unsigned int ImWchar32;     // A single decoded U32 character/code point. We encode them as multi bytes UTF-8 when used in strings.
#ifdef IMGUI_USE_WCHAR32            // ImWchar [configurable type: override in imconfig.h with '#define IMGUI_USE_WCHAR32' to support Unicode planes 1-16]
typedef ImWchar32 ImWchar;
#else
typedef ImWchar16 ImWchar;
#endif
"""
ImWchar = int
ImWchar16 = int
ImWchar32 = int


"""
// Callback and functions types
typedef int     (*ImGuiInputTextCallback)(ImGuiInputTextCallbackData* data);    // Callback function for ImGui::InputText()
typedef void    (*ImGuiSizeCallback)(ImGuiSizeCallbackData* data);              // Callback function for ImGui::SetNextWindowSizeConstraints()
typedef void*   (*ImGuiMemAllocFunc)(size_t sz, void* user_data);               // Function signature for ImGui::SetAllocatorFunctions()
typedef void    (*ImGuiMemFreeFunc)(void* ptr, void* user_data);                // Function signature for ImGui::SetAllocatorFunctions()
"""
"""
#ifndef ImDrawCallback
    typedef void (*ImDrawCallback)(const ImDrawList* parent_list, const ImDrawCmd* cmd);
#endif
"""
ImGuiInputTextCallback = Any       # These types are C function pointers
ImGuiSizeCallback = Any            # and thus are hard to create from python
ImGuiMemAllocFunc = Any
ImGuiMemFreeFunc = Any
ImDrawCallback = Any


"""
// Helpers macros to generate 32-bit encoded colors
// User can declare their own format by #defining the 5 _SHIFT/_MASK macros in their imconfig file.
#ifndef IM_COL32_R_SHIFT
#ifdef IMGUI_USE_BGRA_PACKED_COLOR
#define IM_COL32_R_SHIFT    16
#define IM_COL32_G_SHIFT    8
#define IM_COL32_B_SHIFT    0
#define IM_COL32_A_SHIFT    24
#define IM_COL32_A_MASK     0xFF000000
#else
#define IM_COL32_R_SHIFT    0
#define IM_COL32_G_SHIFT    8
#define IM_COL32_B_SHIFT    16
#define IM_COL32_A_SHIFT    24
#define IM_COL32_A_MASK     0xFF000000
#endif
#endif
#define IM_COL32(R,G,B,A)    (((ImU32)(A)<<IM_COL32_A_SHIFT) | ((ImU32)(B)<<IM_COL32_B_SHIFT) | ((ImU32)(G)<<IM_COL32_G_SHIFT) | ((ImU32)(R)<<IM_COL32_R_SHIFT))
#define IM_COL32_WHITE       IM_COL32(255,255,255,255)  // Opaque white = 0xFFFFFFFF
#define IM_COL32_BLACK       IM_COL32(0,0,0,255)        // Opaque black
#define IM_COL32_BLACK_TRANS IM_COL32(0,0,0,0)          // Transparent black = 0x00000000
"""
IM_COL32_R_SHIFT= 0
IM_COL32_G_SHIFT = 8
IM_COL32_B_SHIFT = 16
IM_COL32_A_SHIFT = 24


def IM_COL32(r: ImU32, g: ImU32, b: ImU32, a: ImU32) -> ImU32:
    r = ((a<<IM_COL32_A_SHIFT) | (b<<IM_COL32_B_SHIFT) | (g<<IM_COL32_G_SHIFT) | (r<<IM_COL32_R_SHIFT))
    return r


IM_COL32_WHITE = IM_COL32(255, 255, 255, 255)
IM_COL32_BLACK = IM_COL32(0, 0, 0, 255)


"""
Additional customizations
"""
ImGuiTextRange = Any # internal structure of ImGuiTextFilter, composed of string pointers (cannot be easily adapted)
ImGuiStoragePair = Any


# Disable black formatter
# fmt: off

##################################################
#    AUTO GENERATED CODE BELOW
##################################################
# <litgen_stub> // Autogenerated code below! Do not edit!
# <Autogenerated_Boxed_Types>
class BoxedFloat:    # imgui.h:1
    value:float                                   # imgui.h:3
    def __init__(self, v: float = 0.) -> None:    # imgui.h:4
        pass
    def __repr__(self) -> str:                    # imgui.h:5
        pass
class BoxedInt:    # imgui.h:1
    value:int                                  # imgui.h:3
    def __init__(self, v: int = 0) -> None:    # imgui.h:4
        pass
    def __repr__(self) -> str:                 # imgui.h:5
        pass
# </Autogenerated_Boxed_Types>



# dear imgui, v1.88 WIP
# (headers)

# Help:
# - Read FAQ at http://dearimgui.org/faq
# - Newcomers, read 'Programmer guide' in imgui.cpp for notes on how to setup Dear ImGui in your codebase.
# - Call and read ImGui::ShowDemoWindow() in imgui_demo.cpp. All applications in examples/ are doing that.
# Read imgui.cpp for details, links and comments.

# Resources:
# - FAQ                   http://dearimgui.org/faq
# - Homepage & latest     https://github.com/ocornut/imgui
# - Releases & changelog  https://github.com/ocornut/imgui/releases
# - Gallery               https://github.com/ocornut/imgui/issues/5243 (please post your screenshots/video there!)
# - Wiki                  https://github.com/ocornut/imgui/wiki (lots of good stuff there)
# - Glossary              https://github.com/ocornut/imgui/wiki/Glossary
# - Issues & support      https://github.com/ocornut/imgui/issues

# Getting Started?
# - For first-time users having issues compiling/linking/running or issues loading fonts:
#   please post in https://github.com/ocornut/imgui/discussions if you cannot find a solution in resources above.

#
#
#Index of this file:
#// [SECTION] Header mess
#// [SECTION] Forward declarations and basic types
#// [SECTION] Dear ImGui end-user API functions
#// [SECTION] Flags & Enumerations
#// [SECTION] Helpers: Memory allocations macros, ImVector<>
#// [SECTION] ImGuiStyle
#// [SECTION] ImGuiIO
#// [SECTION] Misc data structures (ImGuiInputTextCallbackData, ImGuiSizeCallbackData, ImGuiPayload, ImGuiTableSortSpecs, ImGuiTableColumnSortSpecs)
#// [SECTION] Helpers (ImGuiOnceUponAFrame, ImGuiTextFilter, ImGuiTextBuffer, ImGuiStorage, ImGuiListClipper, ImColor)
#// [SECTION] Drawing API (ImDrawCallback, ImDrawCmd, ImDrawIdx, ImDrawVert, ImDrawChannel, ImDrawListSplitter, ImDrawFlags, ImDrawListFlags, ImDrawList, ImDrawData)
#// [SECTION] Font API (ImFontConfig, ImFontGlyph, ImFontGlyphRangesBuilder, ImFontAtlasFlags, ImFontAtlas, ImFont)
#// [SECTION] Viewports (ImGuiViewportFlags, ImGuiViewport)
#// [SECTION] Platform Dependent Interfaces (ImGuiPlatformImeData)
#// [SECTION] Obsolete functions and types
#
#


# Configuration file with compile-time options (edit imconfig.h or '#define IMGUI_USER_CONFIG "myfilename.h" from your build system')


#-----------------------------------------------------------------------------
# [SECTION] Header mess
#-----------------------------------------------------------------------------

# Includes

# Version
# (Integer encoded as XYYZZ for use in #if preprocessor conditionals. Work in progress versions typically starts at XYY99 then bounce up to XYY00, XYY01 etc. when release tagging happens)

# Define attributes of all API symbols declarations (e.g. for DLL under Windows)
# IMGUI_API is used for core imgui functions, IMGUI_IMPL_API is used for the default backends files (imgui_impl_xxx.h)
# Using dear imgui via a shared library is not recommended, because we don't guarantee backward nor forward ABI compatibility (also function call overhead, as dear imgui is a call-heavy API)

# Helper Macros

# Helper Macros - IM_FMTARGS, IM_FMTLIST: Apply printf-style warnings to our formatting functions.

# Disable some of MSVC most aggressive Debug runtime checks in function header/footer (used in some simple/low-level functions)

# Warnings

#-----------------------------------------------------------------------------
# [SECTION] Forward declarations and basic types
#-----------------------------------------------------------------------------

# Forward declarations

# Enums/Flags (declared as int for compatibility with old C++, to allow using as flags without overhead, and to not pollute the top of this file)
# - Tip: Use your programming IDE navigation facilities on the names in the _central column_ below to find the actual flags/enum lists!
#   In Visual Studio IDE: CTRL+comma ("Edit.GoToAll") can follow symbols in comments, whereas CTRL+F12 ("Edit.GoToImplementation") cannot.
#   With Visual Assist installed: ALT+G ("VAssistX.GoToImplementation") can also follow symbols in comments.
# -> enum ImGuiWindowFlags_     // Flags: for Begin(), BeginChild()

# ImTexture: user data for renderer backend to identify a texture [Compile-time configurable type]
# - To use something else than an opaque None* pointer: override with e.g. '#define ImTextureID MyTextureType*' in your imconfig.h file.
# - This can be whatever to you want it to be! read the FAQ about ImTextureID for details.

# ImDrawIdx: vertex index. [Compile-time configurable type]
# - To use 16-bit indices + allow large meshes: backend need to set 'io.BackendFlags |= ImGuiBackendFlags_RendererHasVtxOffset' and handle ImDrawCmd::VtxOffset (recommended).
# - To use 32-bit indices: override with '#define ImDrawIdx unsigned int' in your imconfig.h file.

# Scalar data types

# Character types
# (we generally use UTF-8 encoded string in the API. This is storage specifically for a decoded character used for keyboard input and display)
# A single decoded U32 character/code point. We encode them as multi bytes UTF-8 when used in strings.

# Callback and functions types

class ImVec2:    # imgui.h:251
    x:float                                              # imgui.h:253
    y:float                                              # imgui.h:253
    def __init__(self) -> None:                          # imgui.h:254
        pass
    def __init__(self, _x: float, _y: float) -> None:    # imgui.h:255
        pass
    # We very rarely use this [] operator, the assert overhead is fine.

class ImVec4:    # imgui.h:264
    """ ImVec4: 4D vector used to store clipping rectangles, colors etc. [Compile-time configurable type]"""
    x:float                                                                    # imgui.h:266
    y:float                                                                    # imgui.h:266
    z:float                                                                    # imgui.h:266
    w:float                                                                    # imgui.h:266
    def __init__(self) -> None:                                                # imgui.h:267
        pass
    def __init__(self, _x: float, _y: float, _z: float, _w: float) -> None:    # imgui.h:268
        pass

#-----------------------------------------------------------------------------
# [SECTION] Dear ImGui end-user API functions
# (Note that ImGui:: being a namespace, you can add extra ImGui:: functions in your own separate file. Please don't modify imgui source files!)
#-----------------------------------------------------------------------------

# <Namespace ImGui>
# Context creation and access
# - Each context create its own ImFontAtlas by default. You may instance one yourself and pass it to CreateContext() to share a font atlas between contexts.
# - DLL users: heaps and globals are not shared across DLL boundaries! You will need to call SetCurrentContext() + SetAllocatorFunctions()
#   for each static/DLL boundary you are calling from. Read "Context and Memory Allocators" section of imgui.cpp for details.
def create_context(shared_font_atlas: ImFontAtlas = None) -> ImGuiContext:    # imgui.h:286
    pass
def destroy_context(ctx: ImGuiContext = None) -> None:    # imgui.h:287
    """ None = destroy current context"""
    pass
def get_current_context() -> ImGuiContext:    # imgui.h:288
    pass
def set_current_context(ctx: ImGuiContext) -> None:    # imgui.h:289
    pass

# Main
def get_io() -> ImGuiIO:    # imgui.h:292
    """ access the IO structure (mouse/keyboard/gamepad inputs, time, various configuration options/flags)"""
    pass
def get_style() -> ImGuiStyle:    # imgui.h:293
    """ access the Style structure (colors, sizes). Always use PushStyleCol(), PushStyleVar() to modify style mid-frame!"""
    pass
def new_frame() -> None:    # imgui.h:294
    """ start a new Dear ImGui frame, you can submit any command from this point until Render()/EndFrame()."""
    pass
def end_frame() -> None:    # imgui.h:295
    """ ends the Dear ImGui frame. automatically called by Render(). If you don't need to render data (skipping rendering) you may call EndFrame() without Render()... but you'll have wasted CPU already! If you don't need to render, better to not create any windows and not call NewFrame() at all!"""
    pass
def render() -> None:    # imgui.h:296
    """ ends the Dear ImGui frame, finalize the draw data. You can then get call GetDrawData()."""
    pass
def get_draw_data() -> ImDrawData:    # imgui.h:297
    """ valid after Render() and until the next call to NewFrame(). this is what you have to render."""
    pass

# Demo, Debug, Information
def show_demo_window(p_open: bool = None) -> None:    # imgui.h:300
    """ create Demo window. demonstrate most ImGui features. call this to learn about the library! try to make it always available in your application!"""
    pass
def show_metrics_window(p_open: bool = None) -> None:    # imgui.h:301
    """ create Metrics/Debugger window. display Dear ImGui internals: windows, draw commands, various internal state, etc."""
    pass
def show_stack_tool_window(p_open: bool = None) -> None:    # imgui.h:302
    """ create Stack Tool window. hover items with mouse to query information about the source of their unique ID."""
    pass
def show_about_window(p_open: bool = None) -> None:    # imgui.h:303
    """ create About window. display Dear ImGui version, credits and build/system information."""
    pass
def show_style_editor(ref: ImGuiStyle = None) -> None:    # imgui.h:304
    """ add style editor block (not a window). you can pass in a reference ImGuiStyle structure to compare to, revert to and save to (else it uses the default style)"""
    pass
def show_style_selector(label: str) -> bool:    # imgui.h:305
    """ add style selector block (not a window), essentially a combo listing the default styles."""
    pass
def show_font_selector(label: str) -> None:    # imgui.h:306
    """ add font selector block (not a window), essentially a combo listing the loaded fonts."""
    pass
def show_user_guide() -> None:    # imgui.h:307
    """ add basic help/info block (not a window): how to manipulate ImGui as a end-user (mouse/keyboard controls)."""
    pass
def get_version() -> str:    # imgui.h:308
    """ get the compiled version string e.g. "1.80 WIP" (essentially the value for IMGUI_VERSION from the compiled version of imgui.cpp)"""
    pass

# Styles
def style_colors_dark(dst: ImGuiStyle = None) -> None:    # imgui.h:311
    """ new, recommended style (default)"""
    pass
def style_colors_light(dst: ImGuiStyle = None) -> None:    # imgui.h:312
    """ best used with borders and a custom, thicker font"""
    pass
def style_colors_classic(dst: ImGuiStyle = None) -> None:    # imgui.h:313
    """ classic imgui style"""
    pass

# Windows
# - Begin() = push window to the stack and start appending to it. End() = pop window from the stack.
# - Passing 'bool* p_open != None' shows a window-closing widget in the upper-right corner of the window,
#   which clicking will set the boolean to False when clicked.
# - You may append multiple times to the same window during the same frame by calling Begin()/End() pairs multiple times.
#   Some information such as 'flags' or 'p_open' will only be considered by the first call to Begin().
# - Begin() return False to indicate the window is collapsed or fully clipped, so you may early out and omit submitting
#   anything to the window. Always call a matching End() for each Begin() call, regardless of its return value!
#   [Important: due to legacy reason, this is inconsistent with most other functions such as BeginMenu/EndMenu,
#    BeginPopup/EndPopup, etc. where the EndXXX call should only be called if the corresponding BeginXXX function
#    returned True. Begin and BeginChild are the only odd ones out. Will be fixed in a future update.]
# - Note that the bottom of window stack always contains a window called "Debug".
def begin(name: str, p_open: bool = None, flags: ImGuiWindowFlags = 0) -> bool:    # imgui.h:327
    pass
def end() -> None:    # imgui.h:328
    pass

# Child Windows
# - Use child windows to begin into a self-contained independent scrolling/clipping regions within a host window. Child windows can embed their own child.
# - For each independent axis of 'size': ==0.0: use remaining host window size / >0.0: fixed size / <0.0: use remaining window size minus abs(size) / Each axis can use a different mode, e.g. ImVec2(0,400).
# - BeginChild() returns False to indicate the window is collapsed or fully clipped, so you may early out and omit submitting anything to the window.
#   Always call a matching EndChild() for each BeginChild() call, regardless of its return value.
#   [Important: due to legacy reason, this is inconsistent with most other functions such as BeginMenu/EndMenu,
#    BeginPopup/EndPopup, etc. where the EndXXX call should only be called if the corresponding BeginXXX function
#    returned True. Begin and BeginChild are the only odd ones out. Will be fixed in a future update.]
def begin_child(    # imgui.h:338
    str_id: str,
    size: ImVec2 = ImVec2(0, 0),
    border: bool = False,
    flags: ImGuiWindowFlags = 0
    ) -> bool:
    pass
def begin_child(    # imgui.h:339
    id: ImGuiID,
    size: ImVec2 = ImVec2(0, 0),
    border: bool = False,
    flags: ImGuiWindowFlags = 0
    ) -> bool:
    pass
def end_child() -> None:    # imgui.h:340
    pass

# Windows Utilities
# - 'current window' = the window we are appending into while inside a Begin()/End() block. 'next window' = next window we will Begin() into.
def is_window_appearing() -> bool:    # imgui.h:344
    pass
def is_window_collapsed() -> bool:    # imgui.h:345
    pass
def is_window_focused(flags: ImGuiFocusedFlags = 0) -> bool:    # imgui.h:346
    """ is current window focused? or its root/child, depending on flags. see flags for options."""
    pass
def is_window_hovered(flags: ImGuiHoveredFlags = 0) -> bool:    # imgui.h:347
    """ is current window hovered (and typically: not blocked by a popup/modal)? see flags for options. NB: If you are trying to check whether your mouse should be dispatched to imgui or to your app, you should use the 'io.WantCaptureMouse' boolean for that! Please read the FAQ!"""
    pass
def get_window_draw_list() -> ImDrawList:    # imgui.h:348
    """ get draw list associated to the current window, to append your own drawing primitives"""
    pass
def get_window_pos() -> ImVec2:    # imgui.h:349
    """ get current window position in screen space (useful if you want to do your own drawing via the DrawList API)"""
    pass
def get_window_size() -> ImVec2:    # imgui.h:350
    """ get current window size"""
    pass
def get_window_width() -> float:    # imgui.h:351
    """ get current window width (shortcut for GetWindowSize().x)"""
    pass
def get_window_height() -> float:    # imgui.h:352
    """ get current window height (shortcut for GetWindowSize().y)"""
    pass

# Window manipulation
# - Prefer using SetNextXXX functions (before Begin) rather that SetXXX functions (after Begin).
def set_next_window_pos(    # imgui.h:356
    pos: ImVec2,
    cond: ImGuiCond = 0,
    pivot: ImVec2 = ImVec2(0, 0)
    ) -> None:
    """ set next window position. call before Begin(). use pivot=(0.5,0.5) to center on given point, etc."""
    pass
def set_next_window_size(size: ImVec2, cond: ImGuiCond = 0) -> None:    # imgui.h:357
    """ set next window size. set axis to 0.0 to force an auto-fit on this axis. call before Begin()"""
    pass
def set_next_window_size_constraints(    # imgui.h:358
    size_min: ImVec2,
    size_max: ImVec2,
    custom_callback: ImGuiSizeCallback = None,
    custom_callback_data: None = None
    ) -> None:
    """ set next window size limits. use -1,-1 on either X/Y axis to preserve the current size. Sizes will be rounded down. Use callback to apply non-trivial programmatic constraints."""
    pass
def set_next_window_content_size(size: ImVec2) -> None:    # imgui.h:359
    """ set next window content size (~ scrollable client area, which enforce the range of scrollbars). Not including window decorations (title bar, menu bar, etc.) nor WindowPadding. set an axis to 0.0 to leave it automatic. call before Begin()"""
    pass
def set_next_window_collapsed(collapsed: bool, cond: ImGuiCond = 0) -> None:    # imgui.h:360
    """ set next window collapsed state. call before Begin()"""
    pass
def set_next_window_focus() -> None:    # imgui.h:361
    """ set next window to be focused / top-most. call before Begin()"""
    pass
def set_next_window_bg_alpha(alpha: float) -> None:    # imgui.h:362
    """ set next window background color alpha. helper to easily override the Alpha component of ImGuiCol_WindowBg/ChildBg/PopupBg. you may also use ImGuiWindowFlags_NoBackground."""
    pass
def set_window_pos(pos: ImVec2, cond: ImGuiCond = 0) -> None:    # imgui.h:363
    """ (not recommended) set current window position - call within Begin()/End(). prefer using SetNextWindowPos(), as this may incur tearing and side-effects."""
    pass
def set_window_size(size: ImVec2, cond: ImGuiCond = 0) -> None:    # imgui.h:364
    """ (not recommended) set current window size - call within Begin()/End(). set to ImVec2(0, 0) to force an auto-fit. prefer using SetNextWindowSize(), as this may incur tearing and minor side-effects."""
    pass
def set_window_collapsed(collapsed: bool, cond: ImGuiCond = 0) -> None:    # imgui.h:365
    """ (not recommended) set current window collapsed state. prefer using SetNextWindowCollapsed()."""
    pass
def set_window_focus() -> None:    # imgui.h:366
    """ (not recommended) set current window to be focused / top-most. prefer using SetNextWindowFocus()."""
    pass
def set_window_font_scale(scale: float) -> None:    # imgui.h:367
    """ [OBSOLETE] set font scale. Adjust IO.FontGlobalScale if you want to scale all windows. This is an old API! For correct scaling, prefer to reload font + rebuild ImFontAtlas + call style.ScaleAllSizes()."""
    pass
def set_window_pos(name: str, pos: ImVec2, cond: ImGuiCond = 0) -> None:    # imgui.h:368
    """ set named window position."""
    pass
def set_window_size(name: str, size: ImVec2, cond: ImGuiCond = 0) -> None:    # imgui.h:369
    """ set named window size. set axis to 0.0 to force an auto-fit on this axis."""
    pass
def set_window_collapsed(    # imgui.h:370
    name: str,
    collapsed: bool,
    cond: ImGuiCond = 0
    ) -> None:
    """ set named window collapsed state"""
    pass
def set_window_focus(name: str) -> None:    # imgui.h:371
    """ set named window to be focused / top-most. use None to remove focus."""
    pass

# Content region
# - Retrieve available space from a given point. GetContentRegionAvail() is frequently useful.
# - Those functions are bound to be redesigned (they are confusing, incomplete and the Min/Max return values are in local window coordinates which increases confusion)
def get_content_region_avail() -> ImVec2:    # imgui.h:376
    """ == GetContentRegionMax() - GetCursorPos()"""
    pass
def get_content_region_max() -> ImVec2:    # imgui.h:377
    """ current content boundaries (typically window boundaries including scrolling, or current column boundaries), in windows coordinates"""
    pass
def get_window_content_region_min() -> ImVec2:    # imgui.h:378
    """ content boundaries min for the full window (roughly (0,0)-Scroll), in window coordinates"""
    pass
def get_window_content_region_max() -> ImVec2:    # imgui.h:379
    """ content boundaries max for the full window (roughly (0,0)+Size-Scroll) where Size can be override with SetNextWindowContentSize(), in window coordinates"""
    pass

# Windows Scrolling
def get_scroll_x() -> float:    # imgui.h:382
    """ get scrolling amount [0 .. GetScrollMaxX()]"""
    pass
def get_scroll_y() -> float:    # imgui.h:383
    """ get scrolling amount [0 .. GetScrollMaxY()]"""
    pass
def set_scroll_x(scroll_x: float) -> None:    # imgui.h:384
    """ set scrolling amount [0 .. GetScrollMaxX()]"""
    pass
def set_scroll_y(scroll_y: float) -> None:    # imgui.h:385
    """ set scrolling amount [0 .. GetScrollMaxY()]"""
    pass
def get_scroll_max_x() -> float:    # imgui.h:386
    """ get maximum scrolling amount ~~ ContentSize.x - WindowSize.x - DecorationsSize.x"""
    pass
def get_scroll_max_y() -> float:    # imgui.h:387
    """ get maximum scrolling amount ~~ ContentSize.y - WindowSize.y - DecorationsSize.y"""
    pass
def set_scroll_here_x(center_x_ratio: float = 0.5) -> None:    # imgui.h:388
    """ adjust scrolling amount to make current cursor position visible. center_x_ratio=0.0: left, 0.5: center, 1.0: right. When using to make a "default/current item" visible, consider using SetItemDefaultFocus() instead."""
    pass
def set_scroll_here_y(center_y_ratio: float = 0.5) -> None:    # imgui.h:389
    """ adjust scrolling amount to make current cursor position visible. center_y_ratio=0.0: top, 0.5: center, 1.0: bottom. When using to make a "default/current item" visible, consider using SetItemDefaultFocus() instead."""
    pass
def set_scroll_from_pos_x(local_x: float, center_x_ratio: float = 0.5) -> None:    # imgui.h:390
    """ adjust scrolling amount to make given position visible. Generally GetCursorStartPos() + offset to compute a valid position."""
    pass
def set_scroll_from_pos_y(local_y: float, center_y_ratio: float = 0.5) -> None:    # imgui.h:391
    """ adjust scrolling amount to make given position visible. Generally GetCursorStartPos() + offset to compute a valid position."""
    pass

# Parameters stacks (shared)
def push_font(font: ImFont) -> None:    # imgui.h:394
    """ use None as a shortcut to push default font"""
    pass
def pop_font() -> None:    # imgui.h:395
    pass
def push_style_color(idx: ImGuiCol, col: ImU32) -> None:    # imgui.h:396
    """ modify a style color. always use this if you modify the style after NewFrame()."""
    pass
def push_style_color(idx: ImGuiCol, col: ImVec4) -> None:    # imgui.h:397
    pass
def pop_style_color(count: int = 1) -> None:    # imgui.h:398
    pass
def push_style_var(idx: ImGuiStyleVar, val: float) -> None:    # imgui.h:399
    """ modify a style float variable. always use this if you modify the style after NewFrame()."""
    pass
def push_style_var(idx: ImGuiStyleVar, val: ImVec2) -> None:    # imgui.h:400
    """ modify a style ImVec2 variable. always use this if you modify the style after NewFrame()."""
    pass
def pop_style_var(count: int = 1) -> None:    # imgui.h:401
    pass
def push_allow_keyboard_focus(allow_keyboard_focus: bool) -> None:    # imgui.h:402
    """ == tab stop enable. Allow focusing using TAB/Shift-TAB, enabled by default but you can disable it for certain widgets"""
    pass
def pop_allow_keyboard_focus() -> None:    # imgui.h:403
    pass
def push_button_repeat(repeat: bool) -> None:    # imgui.h:404
    """ in 'repeat' mode, Button*() functions return repeated True in a typematic manner (using io.KeyRepeatDelay/io.KeyRepeatRate setting). Note that you can call IsItemActive() after any Button() to tell if the button is held in the current frame."""
    pass
def pop_button_repeat() -> None:    # imgui.h:405
    pass

# Parameters stacks (current window)
def push_item_width(item_width: float) -> None:    # imgui.h:408
    """ push width of items for common large "item+label" widgets. >0.0: width in pixels, <0.0 align xx pixels to the right of window (so -FLT_MIN always align width to the right side)."""
    pass
def pop_item_width() -> None:    # imgui.h:409
    pass
def set_next_item_width(item_width: float) -> None:    # imgui.h:410
    """ set width of the _next_ common large "item+label" widget. >0.0: width in pixels, <0.0 align xx pixels to the right of window (so -FLT_MIN always align width to the right side)"""
    pass
def calc_item_width() -> float:    # imgui.h:411
    """ width of item given pushed settings and current cursor position. NOT necessarily the width of last item unlike most 'Item' functions."""
    pass
def push_text_wrap_pos(wrap_local_pos_x: float = 0.0) -> None:    # imgui.h:412
    """ push word-wrapping position for Text*() commands. < 0.0: no wrapping; 0.0: wrap to end of window (or column); > 0.0: wrap at 'wrap_pos_x' position in window local space"""
    pass
def pop_text_wrap_pos() -> None:    # imgui.h:413
    pass

# Style read access
# - Use the style editor (ShowStyleEditor() function) to interactively see what the colors are)
def get_font() -> ImFont:    # imgui.h:417
    """ get current font"""
    pass
def get_font_size() -> float:    # imgui.h:418
    """ get current font size (= height in pixels) of current font with current scale applied"""
    pass
def get_font_tex_uv_white_pixel() -> ImVec2:    # imgui.h:419
    """ get UV coordinate for a while pixel, useful to draw custom shapes via the ImDrawList API"""
    pass
def get_color_u32(idx: ImGuiCol, alpha_mul: float = 1.0) -> ImU32:    # imgui.h:420
    """ retrieve given style color with style alpha applied and optional extra alpha multiplier, packed as a 32-bit value suitable for ImDrawList"""
    pass
def get_color_u32(col: ImVec4) -> ImU32:    # imgui.h:421
    """ retrieve given color with style alpha applied, packed as a 32-bit value suitable for ImDrawList"""
    pass
def get_color_u32(col: ImU32) -> ImU32:    # imgui.h:422
    """ retrieve given color with style alpha applied, packed as a 32-bit value suitable for ImDrawList"""
    pass
def get_style_color_vec4(idx: ImGuiCol) -> ImVec4:    # imgui.h:423
    """ retrieve style color as stored in ImGuiStyle structure. use to feed back into PushStyleColor(), otherwise use GetColorU32() to get style color with style alpha baked in."""
    pass

# Cursor / Layout
# - By "cursor" we mean the current output position.
# - The typical widget behavior is to output themselves at the current cursor position, then move the cursor one line down.
# - You can call SameLine() between widgets to undo the last carriage return and output at the right of the preceding widget.
# - Attention! We currently have inconsistencies between window-local and absolute positions we will aim to fix with future API:
#    Window-local coordinates:   SameLine(), GetCursorPos(), SetCursorPos(), GetCursorStartPos(), GetContentRegionMax(), GetWindowContentRegion*(), PushTextWrapPos()
#    Absolute coordinate:        GetCursorScreenPos(), SetCursorScreenPos(), all ImDrawList:: functions.
def separator() -> None:    # imgui.h:432
    """ separator, generally horizontal. inside a menu bar or in horizontal layout mode, this becomes a vertical separator."""
    pass
def same_line(offset_from_start_x: float = 0.0, spacing: float = -1.0) -> None:    # imgui.h:433
    """ call between widgets or groups to layout them horizontally. X position given in window coordinates."""
    pass
def new_line() -> None:    # imgui.h:434
    """ undo a SameLine() or force a new line when in an horizontal-layout context."""
    pass
def spacing() -> None:    # imgui.h:435
    """ add vertical spacing."""
    pass
def dummy(size: ImVec2) -> None:    # imgui.h:436
    """ add a dummy item of given size. unlike InvisibleButton(), Dummy() won't take the mouse click or be navigable into."""
    pass
def indent(indent_w: float = 0.0) -> None:    # imgui.h:437
    """ move content position toward the right, by indent_w, or style.IndentSpacing if indent_w <= 0"""
    pass
def unindent(indent_w: float = 0.0) -> None:    # imgui.h:438
    """ move content position back to the left, by indent_w, or style.IndentSpacing if indent_w <= 0"""
    pass
def begin_group() -> None:    # imgui.h:439
    """ lock horizontal starting position"""
    pass
def end_group() -> None:    # imgui.h:440
    """ unlock horizontal starting position + capture the whole group bounding box into one "item" (so you can use IsItemHovered() or layout primitives such as SameLine() on whole group, etc.)"""
    pass
def get_cursor_pos() -> ImVec2:    # imgui.h:441
    """ cursor position in window coordinates (relative to window position)"""
    pass
def get_cursor_pos_x() -> float:    # imgui.h:442
    """   (some functions are using window-relative coordinates, such as: GetCursorPos, GetCursorStartPos, GetContentRegionMax, GetWindowContentRegion* etc."""
    pass
def get_cursor_pos_y() -> float:    # imgui.h:443
    """    other functions such as GetCursorScreenPos or everything in ImDrawList::"""
    pass
def set_cursor_pos(local_pos: ImVec2) -> None:    # imgui.h:444
    """    are using the main, absolute coordinate system."""
    pass
def set_cursor_pos_x(local_x: float) -> None:    # imgui.h:445
    """    GetWindowPos() + GetCursorPos() == GetCursorScreenPos() etc.)"""
    pass
def set_cursor_pos_y(local_y: float) -> None:    # imgui.h:446
    pass
def get_cursor_start_pos() -> ImVec2:    # imgui.h:447
    """ initial cursor position in window coordinates"""
    pass
def get_cursor_screen_pos() -> ImVec2:    # imgui.h:448
    """ cursor position in absolute coordinates (useful to work with ImDrawList API). generally top-left == GetMainViewport()->Pos == (0,0) in single viewport mode, and bottom-right == GetMainViewport()->Pos+Size == io.DisplaySize in single-viewport mode."""
    pass
def set_cursor_screen_pos(pos: ImVec2) -> None:    # imgui.h:449
    """ cursor position in absolute coordinates"""
    pass
def align_text_to_frame_padding() -> None:    # imgui.h:450
    """ vertically align upcoming text baseline to FramePadding.y so that it will align properly to regularly framed items (call if you have text on a line before a framed item)"""
    pass
def get_text_line_height() -> float:    # imgui.h:451
    """ ~ FontSize"""
    pass
def get_text_line_height_with_spacing() -> float:    # imgui.h:452
    """ ~ FontSize + style.ItemSpacing.y (distance in pixels between 2 consecutive lines of text)"""
    pass
def get_frame_height() -> float:    # imgui.h:453
    """ ~ FontSize + style.FramePadding.y * 2"""
    pass
def get_frame_height_with_spacing() -> float:    # imgui.h:454
    """ ~ FontSize + style.FramePadding.y * 2 + style.ItemSpacing.y (distance in pixels between 2 consecutive lines of framed widgets)"""
    pass

# ID stack/scopes
# Read the FAQ (docs/FAQ.md or http://dearimgui.org/faq) for more details about how ID are handled in dear imgui.
# - Those questions are answered and impacted by understanding of the ID stack system:
#   - "Q: Why is my widget not reacting when I click on it?"
#   - "Q: How can I have widgets with an empty label?"
#   - "Q: How can I have multiple widgets with the same label?"
# - Short version: ID are hashes of the entire ID stack. If you are creating widgets in a loop you most likely
#   want to push a unique identifier (e.g. object pointer, loop index) to uniquely differentiate them.
# - You can also use the "Label##foobar" syntax within widget label to distinguish them from each others.
# - In this header file we use the "label"/"name" terminology to denote a string that will be displayed + used as an ID,
#   whereas "str_id" denote a string that is only used as an ID and not normally displayed.
def push_id(str_id: str) -> None:    # imgui.h:467
    """ push string into the ID stack (will hash string)."""
    pass
def push_id(str_id_begin: str, str_id_end: str) -> None:    # imgui.h:468
    """ push string into the ID stack (will hash string)."""
    pass
def push_id(ptr_id: None) -> None:    # imgui.h:469
    """ push pointer into the ID stack (will hash pointer)."""
    pass
def push_id(int_id: int) -> None:    # imgui.h:470
    """ push integer into the ID stack (will hash integer)."""
    pass
def pop_id() -> None:    # imgui.h:471
    """ pop from the ID stack."""
    pass
def get_id(str_id: str) -> ImGuiID:    # imgui.h:472
    """ calculate unique ID (hash of whole ID stack + given parameter). e.g. if you want to query into ImGuiStorage yourself"""
    pass
def get_id(str_id_begin: str, str_id_end: str) -> ImGuiID:    # imgui.h:473
    pass
def get_id(ptr_id: None) -> ImGuiID:    # imgui.h:474
    pass

# Widgets: Text
def text_unformatted(text: str, text_end: str = None) -> None:    # imgui.h:477
    """ raw text without formatting. Roughly equivalent to Text("%s", text) but: A) doesn't require null terminated string if 'text_end' is specified, B) it's faster, no memory copy is done, no buffer size limits, recommended for long chunks of text."""
    pass
def text(fmt: str) -> None:    # imgui.h:478
    """ formatted text"""
    pass
def text_colored(col: ImVec4, fmt: str) -> None:    # imgui.h:480
    """ shortcut for PushStyleColor(ImGuiCol_Text, col); Text(fmt, ...); PopStyleColor();"""
    pass
def text_disabled(fmt: str) -> None:    # imgui.h:482
    """ shortcut for PushStyleColor(ImGuiCol_Text, style.Colors[ImGuiCol_TextDisabled]); Text(fmt, ...); PopStyleColor();"""
    pass
def text_wrapped(fmt: str) -> None:    # imgui.h:484
    """ shortcut for PushTextWrapPos(0.0); Text(fmt, ...); PopTextWrapPos();. Note that this won't work on an auto-resizing window if there's no other widgets to extend the window width, yoy may need to set a size using SetNextWindowSize()."""
    pass
def label_text(label: str, fmt: str) -> None:    # imgui.h:486
    """ display text+label aligned the same way as value+label widgets"""
    pass
def bullet_text(fmt: str) -> None:    # imgui.h:488
    """ shortcut for Bullet()+Text()"""
    pass

# Widgets: Main
# - Most widgets return True when the value has been changed or when pressed/selected
# - You may also use one of the many IsItemXXX functions (e.g. IsItemActive, IsItemHovered, etc.) to query widget state.
def button(label: str, size: ImVec2 = ImVec2(0, 0)) -> bool:    # imgui.h:494
    """ button"""
    pass
def small_button(label: str) -> bool:    # imgui.h:495
    """ button with FramePadding=(0,0) to easily embed within text"""
    pass
def invisible_button(    # imgui.h:496
    str_id: str,
    size: ImVec2,
    flags: ImGuiButtonFlags = 0
    ) -> bool:
    """ flexible button behavior without the visuals, frequently useful to build custom behaviors using the public api (along with IsItemActive, IsItemHovered, etc.)"""
    pass
def arrow_button(str_id: str, dir: ImGuiDir) -> bool:    # imgui.h:497
    """ square button with an arrow shape"""
    pass
def image(    # imgui.h:498
    user_texture_id: ImTextureID,
    size: ImVec2,
    uv0: ImVec2 = ImVec2(0, 0),
    uv1: ImVec2 = ImVec2(1,1),
    tint_col: ImVec4 = ImVec4(1,1,1,1),
    border_col: ImVec4 = ImVec4(0,0,0,0)
    ) -> None:
    pass
def image_button(    # imgui.h:499
    user_texture_id: ImTextureID,
    size: ImVec2,
    uv0: ImVec2 = ImVec2(0, 0),
    uv1: ImVec2 = ImVec2(1,1),
    frame_padding: int = -1,
    bg_col: ImVec4 = ImVec4(0,0,0,0),
    tint_col: ImVec4 = ImVec4(1,1,1,1)
    ) -> bool:
    """ <0 frame_padding uses default frame padding settings. 0 for no padding"""
    pass
def checkbox(label: str, v: bool) -> bool:    # imgui.h:500
    pass
def checkbox_flags(label: str, flags: int, flags_value: int) -> bool:    # imgui.h:501
    pass
def checkbox_flags(label: str, flags: int, flags_value: int) -> bool:    # imgui.h:502
    pass
def radio_button(label: str, active: bool) -> bool:    # imgui.h:503
    """ use with e.g. if (RadioButton("one", my_value==1)) { my_value = 1; }"""
    pass
def radio_button(label: str, v: int, v_button: int) -> bool:    # imgui.h:504
    """ shortcut to handle the above pattern when value is an integer"""
    pass
def progress_bar(    # imgui.h:505
    fraction: float,
    size_arg: ImVec2 = ImVec2(-sys.float_info.min, 0),
    overlay: str = None
    ) -> None:
    pass
def bullet() -> None:    # imgui.h:506
    """ draw a small circle + keep the cursor on the same line. advance cursor x position by GetTreeNodeToLabelSpacing(), same distance that TreeNode() uses"""
    pass

# Widgets: Combo Box
# - The BeginCombo()/EndCombo() api allows you to manage your contents and selection state however you want it, by creating e.g. Selectable() items.
# - The old Combo() api are helpers over BeginCombo()/EndCombo() which are kept available for convenience purpose. This is analogous to how ListBox are created.
def begin_combo(    # imgui.h:511
    label: str,
    preview_value: str,
    flags: ImGuiComboFlags = 0
    ) -> bool:
    pass
def end_combo() -> None:    # imgui.h:512
    """ only call EndCombo() if BeginCombo() returns True!"""
    pass
def combo(    # imgui.h:513
    label: str,
    current_item: int,
    items: List[str],
    popup_max_height_in_items: int = -1
    ) -> bool:
    pass
def combo(    # imgui.h:514
    label: str,
    current_item: int,
    items_separated_by_zeros: str,
    popup_max_height_in_items: int = -1
    ) -> bool:
    """ Separate items with \0 within a string, end item-list with \0\0. e.g. "One\0Two\0Three\0" """
    pass

# Widgets: Drag Sliders
# - CTRL+Click on any drag box to turn them into an input box. Manually input values aren't clamped by default and can go off-bounds. Use ImGuiSliderFlags_AlwaysClamp to always clamp.
# - For all the Float2/Float3/Float4/Int2/Int3/Int4 versions of every functions, note that a 'float v[X]' function argument is the same as 'float* v',
#   the array syntax is just a way to document the number of elements that are expected to be accessible. You can pass address of your first element out of a contiguous set, e.g. &myvector.x
# - Adjust format string to decorate the value with a prefix, a suffix, or adapt the editing and display precision e.g. "%.3" -> 1.234; "%5.2 secs" -> 01.23 secs; "Biscuit: %.0" -> Biscuit: 1; etc.
# - Format string may also be set to None or use the default format ("%f" or "%d").
# - Speed are per-pixel of mouse movement (v_speed=0.2: mouse needs to move by 5 pixels to increase value by 1). For gamepad/keyboard navigation, minimum speed is Max(v_speed, minimum_step_at_given_precision).
# - Use v_min < v_max to clamp edits to given limits. Note that CTRL+Click manual input can override those limits if ImGuiSliderFlags_AlwaysClamp is not used.
# - Use v_max = FLT_MAX / INT_MAX etc to avoid clamping to a maximum, same with v_min = -FLT_MAX / INT_MIN to avoid clamping to a minimum.
# - We use the same sets of flags for DragXXX() and SliderXXX() functions as the features are the same and it makes it easier to swap them.
# - Legacy: Pre-1.78 there are DragXXX() function signatures that takes a final `float power=1.0' argument instead of the `ImGuiSliderFlags flags=0' argument.
#   If you get a warning converting a float to ImGuiSliderFlags, read https://github.com/ocornut/imgui/issues/3361
def drag_float(    # imgui.h:529
    label: str,
    v: float,
    v_speed: float = 1.0,
    v_min: float = 0.0,
    v_max: float = 0.0,
    format: str = "%.3",
    flags: ImGuiSliderFlags = 0
    ) -> bool:
    """ If v_min >= v_max we have no bound"""
    pass
def drag_float2(    # imgui.h:530
    label: str,
    v_0: BoxedFloat,
    v_1: BoxedFloat,
    v_speed: float = 1.0,
    v_min: float = 0.0,
    v_max: float = 0.0,
    format: str = "%.3",
    flags: ImGuiSliderFlags = 0
    ) -> bool:
    pass
def drag_float3(    # imgui.h:531
    label: str,
    v_0: BoxedFloat,
    v_1: BoxedFloat,
    v_2: BoxedFloat,
    v_speed: float = 1.0,
    v_min: float = 0.0,
    v_max: float = 0.0,
    format: str = "%.3",
    flags: ImGuiSliderFlags = 0
    ) -> bool:
    pass
def drag_float4(    # imgui.h:532
    label: str,
    v_0: BoxedFloat,
    v_1: BoxedFloat,
    v_2: BoxedFloat,
    v_3: BoxedFloat,
    v_speed: float = 1.0,
    v_min: float = 0.0,
    v_max: float = 0.0,
    format: str = "%.3",
    flags: ImGuiSliderFlags = 0
    ) -> bool:
    pass
def drag_float_range2(    # imgui.h:533
    label: str,
    v_current_min: float,
    v_current_max: float,
    v_speed: float = 1.0,
    v_min: float = 0.0,
    v_max: float = 0.0,
    format: str = "%.3",
    format_max: str = None,
    flags: ImGuiSliderFlags = 0
    ) -> bool:
    pass
def drag_int(    # imgui.h:534
    label: str,
    v: int,
    v_speed: float = 1.0,
    v_min: int = 0,
    v_max: int = 0,
    format: str = "%d",
    flags: ImGuiSliderFlags = 0
    ) -> bool:
    """ If v_min >= v_max we have no bound"""
    pass
def drag_int2(    # imgui.h:535
    label: str,
    v_0: BoxedInt,
    v_1: BoxedInt,
    v_speed: float = 1.0,
    v_min: int = 0,
    v_max: int = 0,
    format: str = "%d",
    flags: ImGuiSliderFlags = 0
    ) -> bool:
    pass
def drag_int3(    # imgui.h:536
    label: str,
    v_0: BoxedInt,
    v_1: BoxedInt,
    v_2: BoxedInt,
    v_speed: float = 1.0,
    v_min: int = 0,
    v_max: int = 0,
    format: str = "%d",
    flags: ImGuiSliderFlags = 0
    ) -> bool:
    pass
def drag_int4(    # imgui.h:537
    label: str,
    v_0: BoxedInt,
    v_1: BoxedInt,
    v_2: BoxedInt,
    v_3: BoxedInt,
    v_speed: float = 1.0,
    v_min: int = 0,
    v_max: int = 0,
    format: str = "%d",
    flags: ImGuiSliderFlags = 0
    ) -> bool:
    pass
def drag_int_range2(    # imgui.h:538
    label: str,
    v_current_min: int,
    v_current_max: int,
    v_speed: float = 1.0,
    v_min: int = 0,
    v_max: int = 0,
    format: str = "%d",
    format_max: str = None,
    flags: ImGuiSliderFlags = 0
    ) -> bool:
    pass
def drag_scalar(    # imgui.h:539
    label: str,
    data_type: ImGuiDataType,
    p_data: None,
    v_speed: float = 1.0,
    p_min: None = None,
    p_max: None = None,
    format: str = None,
    flags: ImGuiSliderFlags = 0
    ) -> bool:
    pass
def drag_scalar_n(    # imgui.h:540
    label: str,
    data_type: ImGuiDataType,
    p_data: None,
    components: int,
    v_speed: float = 1.0,
    p_min: None = None,
    p_max: None = None,
    format: str = None,
    flags: ImGuiSliderFlags = 0
    ) -> bool:
    pass

# Widgets: Regular Sliders
# - CTRL+Click on any slider to turn them into an input box. Manually input values aren't clamped by default and can go off-bounds. Use ImGuiSliderFlags_AlwaysClamp to always clamp.
# - Adjust format string to decorate the value with a prefix, a suffix, or adapt the editing and display precision e.g. "%.3" -> 1.234; "%5.2 secs" -> 01.23 secs; "Biscuit: %.0" -> Biscuit: 1; etc.
# - Format string may also be set to None or use the default format ("%f" or "%d").
# - Legacy: Pre-1.78 there are SliderXXX() function signatures that takes a final `float power=1.0' argument instead of the `ImGuiSliderFlags flags=0' argument.
#   If you get a warning converting a float to ImGuiSliderFlags, read https://github.com/ocornut/imgui/issues/3361
def slider_float(    # imgui.h:548
    label: str,
    v: float,
    v_min: float,
    v_max: float,
    format: str = "%.3",
    flags: ImGuiSliderFlags = 0
    ) -> bool:
    """ adjust format to decorate the value with a prefix or a suffix for in-slider labels or unit display."""
    pass
def slider_float2(    # imgui.h:549
    label: str,
    v_0: BoxedFloat,
    v_1: BoxedFloat,
    v_min: float,
    v_max: float,
    format: str = "%.3",
    flags: ImGuiSliderFlags = 0
    ) -> bool:
    pass
def slider_float3(    # imgui.h:550
    label: str,
    v_0: BoxedFloat,
    v_1: BoxedFloat,
    v_2: BoxedFloat,
    v_min: float,
    v_max: float,
    format: str = "%.3",
    flags: ImGuiSliderFlags = 0
    ) -> bool:
    pass
def slider_float4(    # imgui.h:551
    label: str,
    v_0: BoxedFloat,
    v_1: BoxedFloat,
    v_2: BoxedFloat,
    v_3: BoxedFloat,
    v_min: float,
    v_max: float,
    format: str = "%.3",
    flags: ImGuiSliderFlags = 0
    ) -> bool:
    pass
def slider_angle(    # imgui.h:552
    label: str,
    v_rad: float,
    v_degrees_min: float = -360.0,
    v_degrees_max: float = +360.0,
    format: str = "%.0 deg",
    flags: ImGuiSliderFlags = 0
    ) -> bool:
    pass
def slider_int(    # imgui.h:553
    label: str,
    v: int,
    v_min: int,
    v_max: int,
    format: str = "%d",
    flags: ImGuiSliderFlags = 0
    ) -> bool:
    pass
def slider_int2(    # imgui.h:554
    label: str,
    v_0: BoxedInt,
    v_1: BoxedInt,
    v_min: int,
    v_max: int,
    format: str = "%d",
    flags: ImGuiSliderFlags = 0
    ) -> bool:
    pass
def slider_int3(    # imgui.h:555
    label: str,
    v_0: BoxedInt,
    v_1: BoxedInt,
    v_2: BoxedInt,
    v_min: int,
    v_max: int,
    format: str = "%d",
    flags: ImGuiSliderFlags = 0
    ) -> bool:
    pass
def slider_int4(    # imgui.h:556
    label: str,
    v_0: BoxedInt,
    v_1: BoxedInt,
    v_2: BoxedInt,
    v_3: BoxedInt,
    v_min: int,
    v_max: int,
    format: str = "%d",
    flags: ImGuiSliderFlags = 0
    ) -> bool:
    pass
def slider_scalar(    # imgui.h:557
    label: str,
    data_type: ImGuiDataType,
    p_data: None,
    p_min: None,
    p_max: None,
    format: str = None,
    flags: ImGuiSliderFlags = 0
    ) -> bool:
    pass
def slider_scalar_n(    # imgui.h:558
    label: str,
    data_type: ImGuiDataType,
    p_data: None,
    components: int,
    p_min: None,
    p_max: None,
    format: str = None,
    flags: ImGuiSliderFlags = 0
    ) -> bool:
    pass
def v_slider_float(    # imgui.h:559
    label: str,
    size: ImVec2,
    v: float,
    v_min: float,
    v_max: float,
    format: str = "%.3",
    flags: ImGuiSliderFlags = 0
    ) -> bool:
    pass
def v_slider_int(    # imgui.h:560
    label: str,
    size: ImVec2,
    v: int,
    v_min: int,
    v_max: int,
    format: str = "%d",
    flags: ImGuiSliderFlags = 0
    ) -> bool:
    pass
def v_slider_scalar(    # imgui.h:561
    label: str,
    size: ImVec2,
    data_type: ImGuiDataType,
    p_data: None,
    p_min: None,
    p_max: None,
    format: str = None,
    flags: ImGuiSliderFlags = 0
    ) -> bool:
    pass

# Widgets: Input with Keyboard
# - Most of the ImGuiInputTextFlags flags are only useful for InputText() and not for InputFloatX, InputIntX, InputDouble etc.
def input_text(    # imgui.h:565
    label: str,
    str: str,
    flags: ImGuiInputTextFlags = 0,
    callback: ImGuiInputTextCallback = None,
    user_data: None = None
    ) -> bool:
    pass
def input_text_multiline(    # imgui.h:566
    label: str,
    str: str,
    size: ImVec2 = ImVec2(0, 0),
    flags: ImGuiInputTextFlags = 0,
    callback: ImGuiInputTextCallback = None,
    user_data: None = None
    ) -> bool:
    pass
def input_text_with_hint(    # imgui.h:567
    label: str,
    hint: str,
    str: str,
    flags: ImGuiInputTextFlags = 0,
    callback: ImGuiInputTextCallback = None,
    user_data: None = None
    ) -> bool:
    pass

def input_float(    # imgui.h:569
    label: str,
    v: float,
    step: float = 0.0,
    step_fast: float = 0.0,
    format: str = "%.3",
    flags: ImGuiInputTextFlags = 0
    ) -> bool:
    pass
def input_float2(    # imgui.h:570
    label: str,
    v_0: BoxedFloat,
    v_1: BoxedFloat,
    format: str = "%.3",
    flags: ImGuiInputTextFlags = 0
    ) -> bool:
    pass
def input_float3(    # imgui.h:571
    label: str,
    v_0: BoxedFloat,
    v_1: BoxedFloat,
    v_2: BoxedFloat,
    format: str = "%.3",
    flags: ImGuiInputTextFlags = 0
    ) -> bool:
    pass
def input_float4(    # imgui.h:572
    label: str,
    v_0: BoxedFloat,
    v_1: BoxedFloat,
    v_2: BoxedFloat,
    v_3: BoxedFloat,
    format: str = "%.3",
    flags: ImGuiInputTextFlags = 0
    ) -> bool:
    pass
def input_int(    # imgui.h:573
    label: str,
    v: int,
    step: int = 1,
    step_fast: int = 100,
    flags: ImGuiInputTextFlags = 0
    ) -> bool:
    pass
def input_int2(    # imgui.h:574
    label: str,
    v_0: BoxedInt,
    v_1: BoxedInt,
    flags: ImGuiInputTextFlags = 0
    ) -> bool:
    pass
def input_int3(    # imgui.h:575
    label: str,
    v_0: BoxedInt,
    v_1: BoxedInt,
    v_2: BoxedInt,
    flags: ImGuiInputTextFlags = 0
    ) -> bool:
    pass
def input_int4(    # imgui.h:576
    label: str,
    v_0: BoxedInt,
    v_1: BoxedInt,
    v_2: BoxedInt,
    v_3: BoxedInt,
    flags: ImGuiInputTextFlags = 0
    ) -> bool:
    pass
def input_double(    # imgui.h:577
    label: str,
    v: float,
    step: float = 0.0,
    step_fast: float = 0.0,
    format: str = "%.6",
    flags: ImGuiInputTextFlags = 0
    ) -> bool:
    pass
def input_scalar(    # imgui.h:578
    label: str,
    data_type: ImGuiDataType,
    p_data: None,
    p_step: None = None,
    p_step_fast: None = None,
    format: str = None,
    flags: ImGuiInputTextFlags = 0
    ) -> bool:
    pass
def input_scalar_n(    # imgui.h:579
    label: str,
    data_type: ImGuiDataType,
    p_data: None,
    components: int,
    p_step: None = None,
    p_step_fast: None = None,
    format: str = None,
    flags: ImGuiInputTextFlags = 0
    ) -> bool:
    pass

# Widgets: Color Editor/Picker (tip: the ColorEdit* functions have a little color square that can be left-clicked to open a picker, and right-clicked to open an option menu.)
# - Note that in C++ a 'float v[X]' function argument is the _same_ as 'float* v', the array syntax is just a way to document the number of elements that are expected to be accessible.
# - You can pass the address of a first float element out of a contiguous structure, e.g. &myvector.x
def color_edit3(    # imgui.h:584
    label: str,
    col_0: BoxedFloat,
    col_1: BoxedFloat,
    col_2: BoxedFloat,
    flags: ImGuiColorEditFlags = 0
    ) -> bool:
    pass
def color_edit4(    # imgui.h:585
    label: str,
    col_0: BoxedFloat,
    col_1: BoxedFloat,
    col_2: BoxedFloat,
    col_3: BoxedFloat,
    flags: ImGuiColorEditFlags = 0
    ) -> bool:
    pass
def color_picker3(    # imgui.h:586
    label: str,
    col_0: BoxedFloat,
    col_1: BoxedFloat,
    col_2: BoxedFloat,
    flags: ImGuiColorEditFlags = 0
    ) -> bool:
    pass
def color_picker4(    # imgui.h:587
    label: str,
    col_0: BoxedFloat,
    col_1: BoxedFloat,
    col_2: BoxedFloat,
    col_3: BoxedFloat,
    flags: ImGuiColorEditFlags = 0,
    ref_col: float = None
    ) -> bool:
    pass
def color_button(    # imgui.h:588
    desc_id: str,
    col: ImVec4,
    flags: ImGuiColorEditFlags = 0,
    size: ImVec2 = ImVec2(0, 0)
    ) -> bool:
    """ display a color square/button, hover for details, return True when pressed."""
    pass
def set_color_edit_options(flags: ImGuiColorEditFlags) -> None:    # imgui.h:589
    """ initialize current options (generally on application startup) if you want to select a default format, picker type, etc. User will be able to change many settings, unless you pass the _NoOptions flag to your calls."""
    pass

# Widgets: Trees
# - TreeNode functions return True when the node is open, in which case you need to also call TreePop() when you are finished displaying the tree node contents.
def tree_node(label: str) -> bool:    # imgui.h:593
    pass
def tree_node(str_id: str, fmt: str) -> bool:    # imgui.h:594
    """ helper variation to easily decorelate the id from the displayed string. Read the FAQ about why and how to use ID. to align arbitrary text at the same level as a TreeNode() you can use Bullet()."""
    pass
def tree_node(ptr_id: None, fmt: str) -> bool:    # imgui.h:595
    """ " """
    pass
def tree_node_ex(label: str, flags: ImGuiTreeNodeFlags = 0) -> bool:    # imgui.h:598
    pass
def tree_node_ex(str_id: str, flags: ImGuiTreeNodeFlags, fmt: str) -> bool:    # imgui.h:599
    pass
def tree_node_ex(ptr_id: None, flags: ImGuiTreeNodeFlags, fmt: str) -> bool:    # imgui.h:600
    pass
def tree_push(str_id: str) -> None:    # imgui.h:603
    """ ~ Indent()+PushId(). Already called by TreeNode() when returning True, but you can call TreePush/TreePop yourself if desired."""
    pass
def tree_push(ptr_id: None = None) -> None:    # imgui.h:604
    """ " """
    pass
def tree_pop() -> None:    # imgui.h:605
    """ ~ Unindent()+PopId()"""
    pass
def get_tree_node_to_label_spacing() -> float:    # imgui.h:606
    """ horizontal distance preceding label when using TreeNode*() or Bullet() == (g.FontSize + style.FramePadding.x*2) for a regular unframed TreeNode"""
    pass
def collapsing_header(label: str, flags: ImGuiTreeNodeFlags = 0) -> bool:    # imgui.h:607
    """ if returning 'True' the header is open. doesn't indent nor push on ID stack. user doesn't have to call TreePop()."""
    pass
def collapsing_header(    # imgui.h:608
    label: str,
    p_visible: bool,
    flags: ImGuiTreeNodeFlags = 0
    ) -> bool:
    """ when 'p_visible != None': if '*p_visible==True' display an additional small close button on upper right of the header which will set the bool to False when clicked, if '*p_visible==False' don't display the header."""
    pass
def set_next_item_open(is_open: bool, cond: ImGuiCond = 0) -> None:    # imgui.h:609
    """ set next TreeNode/CollapsingHeader open state."""
    pass

# Widgets: Selectables
# - A selectable highlights when hovered, and can display another color when selected.
# - Neighbors selectable extend their highlight bounds in order to leave no gap between them. This is so a series of selected Selectable appear contiguous.
def selectable(    # imgui.h:614
    label: str,
    selected: bool = False,
    flags: ImGuiSelectableFlags = 0,
    size: ImVec2 = ImVec2(0, 0)
    ) -> bool:
    """ "bool selected" carry the selection state (read-only). Selectable() is clicked is returns True so you can modify your selection state. size.x==0.0: use remaining width, size.x>0.0: specify width. size.y==0.0: use label height, size.y>0.0: specify height"""
    pass
def selectable(    # imgui.h:615
    label: str,
    p_selected: bool,
    flags: ImGuiSelectableFlags = 0,
    size: ImVec2 = ImVec2(0, 0)
    ) -> bool:
    """ "bool* p_selected" point to the selection state (read-write), as a convenient helper."""
    pass

# Widgets: List Boxes
# - This is essentially a thin wrapper to using BeginChild/EndChild with some stylistic changes.
# - The BeginListBox()/EndListBox() api allows you to manage your contents and selection state however you want it, by creating e.g. Selectable() or any items.
# - The simplified/old ListBox() api are helpers over BeginListBox()/EndListBox() which are kept available for convenience purpose. This is analoguous to how Combos are created.
# - Choose frame width:   size.x > 0.0: custom  /  size.x < 0.0 or -FLT_MIN: right-align   /  size.x = 0.0 (default): use current ItemWidth
# - Choose frame height:  size.y > 0.0: custom  /  size.y < 0.0 or -FLT_MIN: bottom-align  /  size.y = 0.0 (default): arbitrary default height which can fit ~7 items
def begin_list_box(label: str, size: ImVec2 = ImVec2(0, 0)) -> bool:    # imgui.h:623
    """ open a framed scrolling region"""
    pass
def end_list_box() -> None:    # imgui.h:624
    """ only call EndListBox() if BeginListBox() returned True!"""
    pass
def list_box(    # imgui.h:625
    label: str,
    current_item: int,
    items: List[str],
    height_in_items: int = -1
    ) -> bool:
    pass

# Widgets: Data Plotting
# - Consider using ImPlot (https://github.com/epezent/implot) which is much better!
def plot_lines(    # imgui.h:630
    label: str,
    values: np.ndarray,
    values_offset: int = 0,
    overlay_text: str = None,
    scale_min: float = sys.float_info.max,
    scale_max: float = sys.float_info.max,
    graph_size: ImVec2 = ImVec2(0, 0),
    stride: int = -1
    ) -> None:
    pass
def plot_histogram(    # imgui.h:632
    label: str,
    values: np.ndarray,
    values_offset: int = 0,
    overlay_text: str = None,
    scale_min: float = sys.float_info.max,
    scale_max: float = sys.float_info.max,
    graph_size: ImVec2 = ImVec2(0, 0),
    stride: int = -1
    ) -> None:
    pass

# Widgets: Value() Helpers.
# - Those are merely shortcut to calling Text() with a format string. Output single value in "name: value" format (tip: freely declare more in your code to handle your types. you can add functions to the ImGui namespace)
def value(prefix: str, b: bool) -> None:    # imgui.h:637
    pass
def value(prefix: str, v: int) -> None:    # imgui.h:638
    pass
def value(prefix: str, v: int) -> None:    # imgui.h:639
    pass
def value(prefix: str, v: float, float_format: str = None) -> None:    # imgui.h:640
    pass

# Widgets: Menus
# - Use BeginMenuBar() on a window ImGuiWindowFlags_MenuBar to append to its menu bar.
# - Use BeginMainMenuBar() to create a menu bar at the top of the screen and append to it.
# - Use BeginMenu() to create a menu. You can call BeginMenu() multiple time with the same identifier to append more items to it.
# - Not that MenuItem() keyboardshortcuts are displayed as a convenience but _not processed_ by Dear ImGui at the moment.
def begin_menu_bar() -> bool:    # imgui.h:647
    """ append to menu-bar of current window (requires ImGuiWindowFlags_MenuBar flag set on parent window)."""
    pass
def end_menu_bar() -> None:    # imgui.h:648
    """ only call EndMenuBar() if BeginMenuBar() returns True!"""
    pass
def begin_main_menu_bar() -> bool:    # imgui.h:649
    """ create and append to a full screen menu-bar."""
    pass
def end_main_menu_bar() -> None:    # imgui.h:650
    """ only call EndMainMenuBar() if BeginMainMenuBar() returns True!"""
    pass
def begin_menu(label: str, enabled: bool = True) -> bool:    # imgui.h:651
    """ create a sub-menu entry. only call EndMenu() if this returns True!"""
    pass
def end_menu() -> None:    # imgui.h:652
    """ only call EndMenu() if BeginMenu() returns True!"""
    pass
def menu_item(    # imgui.h:653
    label: str,
    shortcut: str = None,
    selected: bool = False,
    enabled: bool = True
    ) -> bool:
    """ return True when activated."""
    pass
def menu_item(    # imgui.h:654
    label: str,
    shortcut: str,
    p_selected: bool,
    enabled: bool = True
    ) -> bool:
    """ return True when activated + toggle (*p_selected) if p_selected != None"""
    pass

# Tooltips
# - Tooltip are windows following the mouse. They do not take focus away.
def begin_tooltip() -> None:    # imgui.h:658
    """ begin/append a tooltip window. to create full-featured tooltip (with any kind of items)."""
    pass
def end_tooltip() -> None:    # imgui.h:659
    pass
def set_tooltip(fmt: str) -> None:    # imgui.h:660
    """ set a text-only tooltip, typically use with ImGui::IsItemHovered(). override any previous call to SetTooltip()."""
    pass

# Popups, Modals
#  - They block normal mouse hovering detection (and therefore most mouse interactions) behind them.
#  - If not modal: they can be closed by clicking anywhere outside them, or by pressing ESCAPE.
#  - Their visibility state (~bool) is held internally instead of being held by the programmer as we are used to with regular Begin*() calls.
#  - The 3 properties above are related: we need to retain popup visibility state in the library because popups may be closed as any time.
#  - You can bypass the hovering restriction by using ImGuiHoveredFlags_AllowWhenBlockedByPopup when calling IsItemHovered() or IsWindowHovered().
#  - IMPORTANT: Popup identifiers are relative to the current ID stack, so OpenPopup and BeginPopup generally needs to be at the same level of the stack.
#    This is sometimes leading to confusing mistakes. May rework this in the future.

# Popups: begin/end functions
#  - BeginPopup(): query popup state, if open start appending into the window. Call EndPopup() afterwards. ImGuiWindowFlags are forwarded to the window.
#  - BeginPopupModal(): block every interactions behind the window, cannot be closed by user, add a dimming background, has a title bar.
def begin_popup(str_id: str, flags: ImGuiWindowFlags = 0) -> bool:    # imgui.h:675
    """ return True if the popup is open, and you can start outputting to it."""
    pass
def begin_popup_modal(    # imgui.h:676
    name: str,
    p_open: bool = None,
    flags: ImGuiWindowFlags = 0
    ) -> bool:
    """ return True if the modal is open, and you can start outputting to it."""
    pass
def end_popup() -> None:    # imgui.h:677
    """ only call EndPopup() if BeginPopupXXX() returns True!"""
    pass

# Popups: open/close functions
#  - OpenPopup(): set popup state to open. ImGuiPopupFlags are available for opening options.
#  - If not modal: they can be closed by clicking anywhere outside them, or by pressing ESCAPE.
#  - CloseCurrentPopup(): use inside the BeginPopup()/EndPopup() scope to close manually.
#  - CloseCurrentPopup() is called by default by Selectable()/MenuItem() when activated (FIXME: need some options).
#  - Use ImGuiPopupFlags_NoOpenOverExistingPopup to avoid opening a popup if there's already one at the same level. This is equivalent to e.g. testing for !IsAnyPopupOpen() prior to OpenPopup().
#  - Use IsWindowAppearing() after BeginPopup() to tell if a window just opened.
#  - IMPORTANT: Notice that for OpenPopupOnItemClick() we exceptionally default flags to 1 (== ImGuiPopupFlags_MouseButtonRight) for backward compatibility with older API taking 'int mouse_button = 1' parameter
def open_popup(str_id: str, popup_flags: ImGuiPopupFlags = 0) -> None:    # imgui.h:687
    """ call to mark popup as open (don't call every frame!)."""
    pass
def open_popup(id: ImGuiID, popup_flags: ImGuiPopupFlags = 0) -> None:    # imgui.h:688
    """ id overload to facilitate calling from nested stacks"""
    pass
def open_popup_on_item_click(    # imgui.h:689
    str_id: str = None,
    popup_flags: ImGuiPopupFlags = 1
    ) -> None:
    """ helper to open popup when clicked on last item. Default to ImGuiPopupFlags_MouseButtonRight == 1. (note: actually triggers on the mouse _released_ event to be consistent with popup behaviors)"""
    pass
def close_current_popup() -> None:    # imgui.h:690
    """ manually close the popup we have begin-ed into."""
    pass

# Popups: open+begin combined functions helpers
#  - Helpers to do OpenPopup+BeginPopup where the Open action is triggered by e.g. hovering an item and right-clicking.
#  - They are convenient to easily create context menus, hence the name.
#  - IMPORTANT: Notice that BeginPopupContextXXX takes ImGuiPopupFlags just like OpenPopup() and unlike BeginPopup(). For full consistency, we may add ImGuiWindowFlags to the BeginPopupContextXXX functions in the future.
#  - IMPORTANT: Notice that we exceptionally default their flags to 1 (== ImGuiPopupFlags_MouseButtonRight) for backward compatibility with older API taking 'int mouse_button = 1' parameter, so if you add other flags remember to re-add the ImGuiPopupFlags_MouseButtonRight.
def begin_popup_context_item(    # imgui.h:697
    str_id: str = None,
    popup_flags: ImGuiPopupFlags = 1
    ) -> bool:
    """ open+begin popup when clicked on last item. Use str_id==None to associate the popup to previous item. If you want to use that on a non-interactive item such as Text() you need to pass in an explicit ID here. read comments in .cpp!"""
    pass
def begin_popup_context_window(    # imgui.h:698
    str_id: str = None,
    popup_flags: ImGuiPopupFlags = 1
    ) -> bool:
    """ open+begin popup when clicked on current window."""
    pass
def begin_popup_context_void(    # imgui.h:699
    str_id: str = None,
    popup_flags: ImGuiPopupFlags = 1
    ) -> bool:
    """ open+begin popup when clicked in None (where there are no windows)."""
    pass

# Popups: query functions
#  - IsPopupOpen(): return True if the popup is open at the current BeginPopup() level of the popup stack.
#  - IsPopupOpen() with ImGuiPopupFlags_AnyPopupId: return True if any popup is open at the current BeginPopup() level of the popup stack.
#  - IsPopupOpen() with ImGuiPopupFlags_AnyPopupId + ImGuiPopupFlags_AnyPopupLevel: return True if any popup is open.
def is_popup_open(str_id: str, flags: ImGuiPopupFlags = 0) -> bool:    # imgui.h:705
    """ return True if the popup is open."""
    pass

# Tables
# - Full-featured replacement for old Columns API.
# - See Demo->Tables for demo code. See top of imgui_tables.cpp for general commentary.
# - See ImGuiTableFlags_ and ImGuiTableColumnFlags_ enums for a description of available flags.
# The typical call flow is:
# - 1. Call BeginTable(), early out if returning False.
# - 2. Optionally call TableSetupColumn() to submit column name/flags/defaults.
# - 3. Optionally call TableSetupScrollFreeze() to request scroll freezing of columns/rows.
# - 4. Optionally call TableHeadersRow() to submit a header row. Names are pulled from TableSetupColumn() data.
# - 5. Populate contents:
#    - In most situations you can use TableNextRow() + TableSetColumnIndex(N) to start appending into a column.
#    - If you are using tables as a sort of grid, where every columns is holding the same type of contents,
#      you may prefer using TableNextColumn() instead of TableNextRow() + TableSetColumnIndex().
#      TableNextColumn() will automatically wrap-around into the next row if needed.
#    - IMPORTANT: Comparatively to the old Columns() API, we need to call TableNextColumn() for the first column!
#    - Summary of possible call flow:
#        --------------------------------------------------------------------------------------------------------
#        TableNextRow() -> TableSetColumnIndex(0) -> Text("Hello 0") -> TableSetColumnIndex(1) -> Text("Hello 1")  // OK
#        TableNextRow() -> TableNextColumn()      -> Text("Hello 0") -> TableNextColumn()      -> Text("Hello 1")  // OK
#                          TableNextColumn()      -> Text("Hello 0") -> TableNextColumn()      -> Text("Hello 1")  // OK: TableNextColumn() automatically gets to next row!
#        TableNextRow()                           -> Text("Hello 0")                                               // Not OK! Missing TableSetColumnIndex() or TableNextColumn()! Text will not appear!
#        --------------------------------------------------------------------------------------------------------
# - 5. Call EndTable()
def begin_table(    # imgui.h:730
    str_id: str,
    column: int,
    flags: ImGuiTableFlags = 0,
    outer_size: ImVec2 = ImVec2(0.0, 0.0),
    inner_width: float = 0.0
    ) -> bool:
    pass
def end_table() -> None:    # imgui.h:731
    """ only call EndTable() if BeginTable() returns True!"""
    pass
def table_next_row(    # imgui.h:732
    row_flags: ImGuiTableRowFlags = 0,
    min_row_height: float = 0.0
    ) -> None:
    """ append into the first cell of a new row."""
    pass
def table_next_column() -> bool:    # imgui.h:733
    """ append into the next column (or first column of next row if currently in last column). Return True when column is visible."""
    pass
def table_set_column_index(column_n: int) -> bool:    # imgui.h:734
    """ append into the specified column. Return True when column is visible."""
    pass

# Tables: Headers & Columns declaration
# - Use TableSetupColumn() to specify label, resizing policy, default width/weight, id, various other flags etc.
# - Use TableHeadersRow() to create a header row and automatically submit a TableHeader() for each column.
#   Headers are required to perform: reordering, sorting, and opening the context menu.
#   The context menu can also be made available in columns body using ImGuiTableFlags_ContextMenuInBody.
# - You may manually submit headers using TableNextRow() + TableHeader() calls, but this is only useful in
#   some advanced use cases (e.g. adding custom widgets in header row).
# - Use TableSetupScrollFreeze() to lock columns/rows so they stay visible when scrolled.
def table_setup_column(    # imgui.h:744
    label: str,
    flags: ImGuiTableColumnFlags = 0,
    init_width_or_weight: float = 0.0,
    user_id: ImGuiID = 0
    ) -> None:
    pass
def table_setup_scroll_freeze(cols: int, rows: int) -> None:    # imgui.h:745
    """ lock columns/rows so they stay visible when scrolled."""
    pass
def table_headers_row() -> None:    # imgui.h:746
    """ submit all headers cells based on data provided to TableSetupColumn() + submit context menu"""
    pass
def table_header(label: str) -> None:    # imgui.h:747
    """ submit one header cell manually (rarely used)"""
    pass

# Tables: Sorting & Miscellaneous functions
# - Sorting: call TableGetSortSpecs() to retrieve latest sort specs for the table. None when not sorting.
#   When 'sort_specs->SpecsDirty == True' you should sort your data. It will be True when sorting specs have
#   changed since last call, or the first time. Make sure to set 'SpecsDirty = False' after sorting,
#   else you may wastefully sort your data every frame!
# - Functions args 'int column_n' treat the default value of -1 as the same as passing the current column index.
def table_get_sort_specs() -> ImGuiTableSortSpecs:    # imgui.h:755
    """ get latest sort specs for the table (None if not sorting).  Lifetime: don't hold on this pointer over multiple frames or past any subsequent call to BeginTable()."""
    pass
def table_get_column_count() -> int:    # imgui.h:756
    """ return number of columns (value passed to BeginTable)"""
    pass
def table_get_column_index() -> int:    # imgui.h:757
    """ return current column index."""
    pass
def table_get_row_index() -> int:    # imgui.h:758
    """ return current row index."""
    pass
def table_get_column_name(column_n: int = -1) -> str:    # imgui.h:759
    """ return "" if column didn't have a name declared by TableSetupColumn(). Pass -1 to use current column."""
    pass
def table_get_column_flags(column_n: int = -1) -> ImGuiTableColumnFlags:    # imgui.h:760
    """ return column flags so you can query their Enabled/Visible/Sorted/Hovered status flags. Pass -1 to use current column."""
    pass
def table_set_column_enabled(column_n: int, v: bool) -> None:    # imgui.h:761
    """ change user accessible enabled/disabled state of a column. Set to False to hide the column. User can use the context menu to change this themselves (right-click in headers, or right-click in columns body with ImGuiTableFlags_ContextMenuInBody)"""
    pass
def table_set_bg_color(    # imgui.h:762
    target: ImGuiTableBgTarget,
    color: ImU32,
    column_n: int = -1
    ) -> None:
    """ change the color of a cell, row, or column. See ImGuiTableBgTarget_ flags for details."""
    pass

# Legacy Columns API (prefer using Tables!)
# - You can also use SameLine(pos_x) to mimic simplified columns.
def columns(count: int = 1, id: str = None, border: bool = True) -> None:    # imgui.h:766
    pass
def next_column() -> None:    # imgui.h:767
    """ next column, defaults to current row or next row if the current row is finished"""
    pass
def get_column_index() -> int:    # imgui.h:768
    """ get current column index"""
    pass
def get_column_width(column_index: int = -1) -> float:    # imgui.h:769
    """ get column width (in pixels). pass -1 to use current column"""
    pass
def set_column_width(column_index: int, width: float) -> None:    # imgui.h:770
    """ set column width (in pixels). pass -1 to use current column"""
    pass
def get_column_offset(column_index: int = -1) -> float:    # imgui.h:771
    """ get position of column line (in pixels, from the left side of the contents region). pass -1 to use current column, otherwise 0..GetColumnsCount() inclusive. column 0 is typically 0.0"""
    pass
def set_column_offset(column_index: int, offset_x: float) -> None:    # imgui.h:772
    """ set position of column line (in pixels, from the left side of the contents region). pass -1 to use current column"""
    pass
def get_columns_count() -> int:    # imgui.h:773
    pass

# Tab Bars, Tabs
def begin_tab_bar(str_id: str, flags: ImGuiTabBarFlags = 0) -> bool:    # imgui.h:776
    """ create and append into a TabBar"""
    pass
def end_tab_bar() -> None:    # imgui.h:777
    """ only call EndTabBar() if BeginTabBar() returns True!"""
    pass
def begin_tab_item(    # imgui.h:778
    label: str,
    p_open: bool = None,
    flags: ImGuiTabItemFlags = 0
    ) -> bool:
    """ create a Tab. Returns True if the Tab is selected."""
    pass
def end_tab_item() -> None:    # imgui.h:779
    """ only call EndTabItem() if BeginTabItem() returns True!"""
    pass
def tab_item_button(label: str, flags: ImGuiTabItemFlags = 0) -> bool:    # imgui.h:780
    """ create a Tab behaving like a button. return True when clicked. cannot be selected in the tab bar."""
    pass
def set_tab_item_closed(tab_or_docked_window_label: str) -> None:    # imgui.h:781
    """ notify TabBar or Docking system of a closed tab/window ahead (useful to reduce visual flicker on reorderable tab bars). For tab-bar: call after BeginTabBar() and before Tab submissions. Otherwise call with a window name."""
    pass

# Logging/Capture
# - All text output from the interface can be captured into tty/file/clipboard. By default, tree nodes are automatically opened during logging.
def log_to_tty(auto_open_depth: int = -1) -> None:    # imgui.h:785
    """ start logging to tty (stdout)"""
    pass
def log_to_file(auto_open_depth: int = -1, filename: str = None) -> None:    # imgui.h:786
    """ start logging to file"""
    pass
def log_to_clipboard(auto_open_depth: int = -1) -> None:    # imgui.h:787
    """ start logging to OS clipboard"""
    pass
def log_finish() -> None:    # imgui.h:788
    """ stop logging (close file, etc.)"""
    pass
def log_buttons() -> None:    # imgui.h:789
    """ helper to display buttons for logging to tty/file/clipboard"""
    pass
def log_text(fmt: str) -> None:    # imgui.h:790
    """ pass text data straight to log (without being displayed)"""
    pass

# Drag and Drop
# - On source items, call BeginDragDropSource(), if it returns True also call SetDragDropPayload() + EndDragDropSource().
# - On target candidates, call BeginDragDropTarget(), if it returns True also call AcceptDragDropPayload() + EndDragDropTarget().
# - If you stop calling BeginDragDropSource() the payload is preserved however it won't have a preview tooltip (we currently display a fallback "..." tooltip, see #1725)
# - An item can be both drag source and drop target.
def begin_drag_drop_source(flags: ImGuiDragDropFlags = 0) -> bool:    # imgui.h:798
    """ call after submitting an item which may be dragged. when this return True, you can call SetDragDropPayload() + EndDragDropSource()"""
    pass
def set_drag_drop_payload(    # imgui.h:799
    type: str,
    data: None,
    sz: int,
    cond: ImGuiCond = 0
    ) -> bool:
    """ type is a user defined string of maximum 32 characters. Strings starting with '_' are reserved for dear imgui internal types. Data is copied and held by imgui. Return True when payload has been accepted."""
    pass
def end_drag_drop_source() -> None:    # imgui.h:800
    """ only call EndDragDropSource() if BeginDragDropSource() returns True!"""
    pass
def begin_drag_drop_target() -> bool:    # imgui.h:801
    """ call after submitting an item that may receive a payload. If this returns True, you can call AcceptDragDropPayload() + EndDragDropTarget()"""
    pass
def accept_drag_drop_payload(    # imgui.h:802
    type: str,
    flags: ImGuiDragDropFlags = 0
    ) -> ImGuiPayload:
    """ accept contents of a given type. If ImGuiDragDropFlags_AcceptBeforeDelivery is set you can peek into the payload before the mouse button is released."""
    pass
def end_drag_drop_target() -> None:    # imgui.h:803
    """ only call EndDragDropTarget() if BeginDragDropTarget() returns True!"""
    pass
def get_drag_drop_payload() -> ImGuiPayload:    # imgui.h:804
    """ peek directly into the current payload from anywhere. may return None. use ImGuiPayload::IsDataType() to test for the payload type."""
    pass

# Disabling [BETA API]
# - Disable all user interactions and dim items visuals (applying style.DisabledAlpha over current colors)
# - Those can be nested but it cannot be used to enable an already disabled section (a single BeginDisabled(True) in the stack is enough to keep everything disabled)
# - BeginDisabled(False) essentially does nothing useful but is provided to facilitate use of boolean expressions. If you can avoid calling BeginDisabled(False)/EndDisabled() best to avoid it.
def begin_disabled(disabled: bool = True) -> None:    # imgui.h:810
    pass
def end_disabled() -> None:    # imgui.h:811
    pass

# Clipping
# - Mouse hovering is affected by ImGui::PushClipRect() calls, unlike direct calls to ImDrawList::PushClipRect() which are render only.
def push_clip_rect(    # imgui.h:815
    clip_rect_min: ImVec2,
    clip_rect_max: ImVec2,
    intersect_with_current_clip_rect: bool
    ) -> None:
    pass
def pop_clip_rect() -> None:    # imgui.h:816
    pass

# Focus, Activation
# - Prefer using "SetItemDefaultFocus()" over "if (IsWindowAppearing()) SetScrollHereY()" when applicable to signify "this is the default item"
def set_item_default_focus() -> None:    # imgui.h:820
    """ make last item the default focused item of a window."""
    pass
def set_keyboard_focus_here(offset: int = 0) -> None:    # imgui.h:821
    """ focus keyboard on the next widget. Use positive 'offset' to access sub components of a multiple component widget. Use -1 to access previous widget."""
    pass

# Item/Widgets Utilities and Query Functions
# - Most of the functions are referring to the previous Item that has been submitted.
# - See Demo Window under "Widgets->Querying Status" for an interactive visualization of most of those functions.
def is_item_hovered(flags: ImGuiHoveredFlags = 0) -> bool:    # imgui.h:826
    """ is the last item hovered? (and usable, aka not blocked by a popup, etc.). See ImGuiHoveredFlags for more options."""
    pass
def is_item_active() -> bool:    # imgui.h:827
    """ is the last item active? (e.g. button being held, text field being edited. This will continuously return True while holding mouse button on an item. Items that don't interact will always return False)"""
    pass
def is_item_focused() -> bool:    # imgui.h:828
    """ is the last item focused for keyboard/gamepad navigation?"""
    pass
def is_item_clicked(mouse_button: ImGuiMouseButton = 0) -> bool:    # imgui.h:829
    """ is the last item hovered and mouse clicked on? (**)  == IsMouseClicked(mouse_button) && IsItemHovered()Important. (**) this it NOT equivalent to the behavior of e.g. Button(). Read comments in function definition."""
    pass
def is_item_visible() -> bool:    # imgui.h:830
    """ is the last item visible? (items may be out of sight because of clipping/scrolling)"""
    pass
def is_item_edited() -> bool:    # imgui.h:831
    """ did the last item modify its underlying value this frame? or was pressed? This is generally the same as the "bool" return value of many widgets."""
    pass
def is_item_activated() -> bool:    # imgui.h:832
    """ was the last item just made active (item was previously inactive)."""
    pass
def is_item_deactivated() -> bool:    # imgui.h:833
    """ was the last item just made inactive (item was previously active). Useful for Undo/Redo patterns with widgets that requires continuous editing."""
    pass
def is_item_deactivated_after_edit() -> bool:    # imgui.h:834
    """ was the last item just made inactive and made a value change when it was active? (e.g. Slider/Drag moved). Useful for Undo/Redo patterns with widgets that requires continuous editing. Note that you may get False positives (some widgets such as Combo()/ListBox()/Selectable() will return True even when clicking an already selected item)."""
    pass
def is_item_toggled_open() -> bool:    # imgui.h:835
    """ was the last item open state toggled? set by TreeNode()."""
    pass
def is_any_item_hovered() -> bool:    # imgui.h:836
    """ is any item hovered?"""
    pass
def is_any_item_active() -> bool:    # imgui.h:837
    """ is any item active?"""
    pass
def is_any_item_focused() -> bool:    # imgui.h:838
    """ is any item focused?"""
    pass
def get_item_rect_min() -> ImVec2:    # imgui.h:839
    """ get upper-left bounding rectangle of the last item (screen space)"""
    pass
def get_item_rect_max() -> ImVec2:    # imgui.h:840
    """ get lower-right bounding rectangle of the last item (screen space)"""
    pass
def get_item_rect_size() -> ImVec2:    # imgui.h:841
    """ get size of last item"""
    pass
def set_item_allow_overlap() -> None:    # imgui.h:842
    """ allow last item to be overlapped by a subsequent item. sometimes useful with invisible buttons, selectables, etc. to catch unused area."""
    pass

# Viewports
# - Currently represents the Platform Window created by the application which is hosting our Dear ImGui windows.
# - In 'docking' branch with multi-viewport enabled, we extend this concept to have multiple active viewports.
# - In the future we will extend this concept further to also represent Platform Monitor and support a "no main platform window" operation mode.
def get_main_viewport() -> ImGuiViewport:    # imgui.h:848
    """ return primary/default viewport. This can never be None."""
    pass

# Background/Foreground Draw Lists
def get_background_draw_list() -> ImDrawList:    # imgui.h:851
    """ this draw list will be the first rendered one. Useful to quickly draw shapes/text behind dear imgui contents."""
    pass
def get_foreground_draw_list() -> ImDrawList:    # imgui.h:852
    """ this draw list will be the last rendered one. Useful to quickly draw shapes/text over dear imgui contents."""
    pass

# Miscellaneous Utilities
def is_rect_visible(size: ImVec2) -> bool:    # imgui.h:855
    """ test if rectangle (of given size, starting from cursor position) is visible / not clipped."""
    pass
def is_rect_visible(rect_min: ImVec2, rect_max: ImVec2) -> bool:    # imgui.h:856
    """ test if rectangle (in screen space) is visible / not clipped. to perform coarse clipping on user's side."""
    pass
def get_time() -> float:    # imgui.h:857
    """ get global imgui time. incremented by io.DeltaTime every frame."""
    pass
def get_frame_count() -> int:    # imgui.h:858
    """ get global imgui frame count. incremented by 1 every frame."""
    pass
def get_draw_list_shared_data() -> ImDrawListSharedData:    # imgui.h:859
    """ you may use this when creating your own ImDrawList instances."""
    pass
def get_style_color_name(idx: ImGuiCol) -> str:    # imgui.h:860
    """ get a string corresponding to the enum value (for display, saving, etc.)."""
    pass
def set_state_storage(storage: ImGuiStorage) -> None:    # imgui.h:861
    """ replace current window storage with our own (if you want to manipulate it yourself, typically clear subsection of it)"""
    pass
def get_state_storage() -> ImGuiStorage:    # imgui.h:862
    pass
def begin_child_frame(    # imgui.h:863
    id: ImGuiID,
    size: ImVec2,
    flags: ImGuiWindowFlags = 0
    ) -> bool:
    """ helper to create a child window / scrolling region that looks like a normal widget frame"""
    pass
def end_child_frame() -> None:    # imgui.h:864
    """ always call EndChildFrame() regardless of BeginChildFrame() return values (which indicates a collapsed/clipped window)"""
    pass

def calc_text_size(    # imgui.h:867
    text: str,
    text_end: str = None,
    hide_text_after_double_hash: bool = False,
    wrap_width: float = -1.0
    ) -> ImVec2:
    """ Text Utilities"""
    pass

# Color Utilities
def color_convert_u32_to_float4(in_: ImU32) -> ImVec4:    # imgui.h:870
    pass
def color_convert_float4_to_u32(in_: ImVec4) -> ImU32:    # imgui.h:871
    pass
def color_convert_hs_vto_rgb(    # imgui.h:873
    h: float,
    s: float,
    v: float,
    out_r: float,
    out_g: float,
    out_b: float
    ) -> None:
    pass

# Inputs Utilities: Keyboard
# Without IMGUI_DISABLE_OBSOLETE_KEYIO: (legacy support)
#   - For 'ImGuiKey key' you can still use your legacy native/user indices according to how your backend/engine stored them in io.KeysDown[].
# With IMGUI_DISABLE_OBSOLETE_KEYIO: (this is the way forward)
#   - Any use of 'ImGuiKey' will assert when key < 512 will be passed, previously reserved as native/user keys indices
#   - GetKeyIndex() is pass-through and therefore deprecated (gone if IMGUI_DISABLE_OBSOLETE_KEYIO is defined)
def is_key_down(key: ImGuiKey) -> bool:    # imgui.h:881
    """ is key being held."""
    pass
def is_key_pressed(key: ImGuiKey, repeat: bool = True) -> bool:    # imgui.h:882
    """ was key pressed (went from !Down to Down)? if repeat=True, uses io.KeyRepeatDelay / KeyRepeatRate"""
    pass
def is_key_released(key: ImGuiKey) -> bool:    # imgui.h:883
    """ was key released (went from Down to !Down)?"""
    pass
def get_key_pressed_amount(    # imgui.h:884
    key: ImGuiKey,
    repeat_delay: float,
    rate: float
    ) -> int:
    """ uses provided repeat rate/delay. return a count, most often 0 or 1 but might be >1 if RepeatRate is small enough that DeltaTime > RepeatRate"""
    pass
def get_key_name(key: ImGuiKey) -> str:    # imgui.h:885
    """ [DEBUG] returns English name of the key. Those names a provided for debugging purpose and are not meant to be saved persistently not compared."""
    pass
def set_next_frame_want_capture_keyboard(want_capture_keyboard: bool) -> None:    # imgui.h:886
    """ Override io.WantCaptureKeyboard flag next frame (said flag is left for your application to handle, typically when True it instructs your app to ignore inputs). e.g. force capture keyboard when your widget is being hovered. This is equivalent to setting "io.WantCaptureKeyboard = want_capture_keyboard"; after the next NewFrame() call."""
    pass

# Inputs Utilities: Mouse
# - To refer to a mouse button, you may use named enums in your code e.g. ImGuiMouseButton_Left, ImGuiMouseButton_Right.
# - You can also use regular integer: it is forever guaranteed that 0=Left, 1=Right, 2=Middle.
# - Dragging operations are only reported after mouse has moved a certain distance away from the initial clicking position (see 'lock_threshold' and 'io.MouseDraggingThreshold')
def is_mouse_down(button: ImGuiMouseButton) -> bool:    # imgui.h:892
    """ is mouse button held?"""
    pass
def is_mouse_clicked(button: ImGuiMouseButton, repeat: bool = False) -> bool:    # imgui.h:893
    """ did mouse button clicked? (went from !Down to Down). Same as GetMouseClickedCount() == 1."""
    pass
def is_mouse_released(button: ImGuiMouseButton) -> bool:    # imgui.h:894
    """ did mouse button released? (went from Down to !Down)"""
    pass
def is_mouse_double_clicked(button: ImGuiMouseButton) -> bool:    # imgui.h:895
    """ did mouse button double-clicked? Same as GetMouseClickedCount() == 2. (note that a double-click will also report IsMouseClicked() == True)"""
    pass
def get_mouse_clicked_count(button: ImGuiMouseButton) -> int:    # imgui.h:896
    """ return the number of successive mouse-clicks at the time where a click happen (otherwise 0)."""
    pass
def is_mouse_hovering_rect(    # imgui.h:897
    r_min: ImVec2,
    r_max: ImVec2,
    clip: bool = True
    ) -> bool:
    """ is mouse hovering given bounding rect (in screen space). clipped by current clipping settings, but disregarding of other consideration of focus/window ordering/popup-block."""
    pass
def is_mouse_pos_valid(mouse_pos: ImVec2 = None) -> bool:    # imgui.h:898
    """ by convention we use (-FLT_MAX,-FLT_MAX) to denote that there is no mouse available"""
    pass
def is_any_mouse_down() -> bool:    # imgui.h:899
    """ [WILL OBSOLETE] is any mouse button held? This was designed for backends, but prefer having backend maintain a mask of held mouse buttons, because upcoming input queue system will make this invalid."""
    pass
def get_mouse_pos() -> ImVec2:    # imgui.h:900
    """ shortcut to ImGui::GetIO().MousePos provided by user, to be consistent with other calls"""
    pass
def get_mouse_pos_on_opening_current_popup() -> ImVec2:    # imgui.h:901
    """ retrieve mouse position at the time of opening popup we have BeginPopup() into (helper to avoid user backing that value themselves)"""
    pass
def is_mouse_dragging(    # imgui.h:902
    button: ImGuiMouseButton,
    lock_threshold: float = -1.0
    ) -> bool:
    """ is mouse dragging? (if lock_threshold < -1.0, uses io.MouseDraggingThreshold)"""
    pass
def get_mouse_drag_delta(    # imgui.h:903
    button: ImGuiMouseButton = 0,
    lock_threshold: float = -1.0
    ) -> ImVec2:
    """ return the delta from the initial clicking position while the mouse button is pressed or was just released. This is locked and return 0.0 until the mouse moves past a distance threshold at least once (if lock_threshold < -1.0, uses io.MouseDraggingThreshold)"""
    pass
def reset_mouse_drag_delta(button: ImGuiMouseButton = 0) -> None:    # imgui.h:904
    pass
def get_mouse_cursor() -> ImGuiMouseCursor:    # imgui.h:905
    """ get desired cursor type, reset in ImGui::NewFrame(), this is updated during the frame. valid before Render(). If you use software rendering by setting io.MouseDrawCursor ImGui will render those for you"""
    pass
def set_mouse_cursor(cursor_type: ImGuiMouseCursor) -> None:    # imgui.h:906
    """ set desired cursor type"""
    pass
def set_next_frame_want_capture_mouse(want_capture_mouse: bool) -> None:    # imgui.h:907
    """ Override io.WantCaptureMouse flag next frame (said flag is left for your application to handle, typical when True it instucts your app to ignore inputs). This is equivalent to setting "io.WantCaptureMouse = want_capture_mouse;" after the next NewFrame() call."""
    pass

# Clipboard Utilities
# - Also see the LogToClipboard() function to capture GUI into clipboard, or easily output text data to the clipboard.
def get_clipboard_text() -> str:    # imgui.h:911
    pass
def set_clipboard_text(text: str) -> None:    # imgui.h:912
    pass

# Settings/.Ini Utilities
# - The disk functions are automatically called if io.IniFilename != None (default is "imgui.ini").
# - Set io.IniFilename to None to load/save manually. Read io.WantSaveIniSettings description about handling .ini saving manually.
# - Important: default value "imgui.ini" is relative to current working dir! Most apps will want to lock this to an absolute path (e.g. same path as executables).
def load_ini_settings_from_disk(ini_filename: str) -> None:    # imgui.h:918
    """ call after CreateContext() and before the first call to NewFrame(). NewFrame() automatically calls LoadIniSettingsFromDisk(io.IniFilename)."""
    pass
def load_ini_settings_from_memory(ini_data: str, ini_size: int = 0) -> None:    # imgui.h:919
    """ call after CreateContext() and before the first call to NewFrame() to provide .ini data from your own data source."""
    pass
def save_ini_settings_to_disk(ini_filename: str) -> None:    # imgui.h:920
    """ this is automatically called (if io.IniFilename is not empty) a few seconds after any modification that should be reflected in the .ini file (and also by DestroyContext)."""
    pass
def save_ini_settings_to_memory(out_ini_size: int = None) -> str:    # imgui.h:921
    """ return a zero-terminated string with the .ini data which you can save by your own mean. call when io.WantSaveIniSettings is set, then save data by your own mean and clear io.WantSaveIniSettings."""
    pass

# Debug Utilities
def debug_text_encoding(text: str) -> None:    # imgui.h:924
    pass
def debug_check_version_and_data_layout(    # imgui.h:925
    version_str: str,
    sz_io: int,
    sz_style: int,
    sz_vec2: int,
    sz_vec4: int,
    sz_drawvert: int,
    sz_drawidx: int
    ) -> bool:
    """ This is called by IMGUI_CHECKVERSION() macro."""
    pass

# Memory Allocators
# - Those functions are not reliant on the current context.
# - DLL users: heaps and globals are not shared across DLL boundaries! You will need to call SetCurrentContext() + SetAllocatorFunctions()
#   for each static/DLL boundary you are calling from. Read "Context and Memory Allocators" section of imgui.cpp for more details.

# </Namespace ImGui>

#-----------------------------------------------------------------------------
# [SECTION] Flags & Enumerations
#-----------------------------------------------------------------------------

class ImGuiWindowFlags_(Enum):    # imgui.h:943
    """ Flags for ImGui::Begin()"""
    none = 0
    no_title_bar = 1 << 0                 # Disable title-bar
    no_resize = 1 << 1                    # Disable user resizing with the lower-right grip
    no_move = 1 << 2                      # Disable user moving the window
    no_scrollbar = 1 << 3                 # Disable scrollbars (window can still scroll with mouse or programmatically)
    no_scroll_with_mouse = 1 << 4         # Disable user vertically scrolling with mouse wheel. On child window, mouse wheel will be forwarded to the parent unless NoScrollbar is also set.
    no_collapse = 1 << 5                  # Disable user collapsing window by double-clicking on it. Also referred to as Window Menu Button (e.g. within a docking node).
    always_auto_resize = 1 << 6           # Resize every window to its content every frame
    no_background = 1 << 7                # Disable drawing background color (WindowBg, etc.) and outside border. Similar as using SetNextWindowBgAlpha(0.0).
    no_saved_settings = 1 << 8            # Never load/save settings in .ini file
    no_mouse_inputs = 1 << 9              # Disable catching mouse, hovering test with pass through.
    menu_bar = 1 << 10                    # Has a menu-bar
    horizontal_scrollbar = 1 << 11        # Allow horizontal scrollbar to appear (off by default). You may use SetNextWindowContentSize(ImVec2(width,0.0)); prior to calling Begin() to specify width. Read code in imgui_demo in the "Horizontal Scrolling" section.
    no_focus_on_appearing = 1 << 12       # Disable taking focus when transitioning from hidden to visible state
    no_bring_to_front_on_focus = 1 << 13  # Disable bringing window to front when taking focus (e.g. clicking on it or programmatically giving it focus)
    always_vertical_scrollbar = 1 << 14   # Always show vertical scrollbar (even if ContentSize.y < Size.y)
    always_horizontal_scrollbar = 1<< 15  # Always show horizontal scrollbar (even if ContentSize.x < Size.x)
    always_use_window_padding = 1 << 16   # Ensure child windows without border uses style.WindowPadding (ignored by default for non-bordered child windows, because more convenient)
    no_nav_inputs = 1 << 18               # No gamepad/keyboard navigation within the window
    no_nav_focus = 1 << 19                # No focusing toward this window with gamepad/keyboard navigation (e.g. skipped by CTRL+TAB)
    unsaved_document = 1 << 20            # Display a dot next to the title. When used in a tab/docking context, tab is selected when clicking the X + closure is not assumed (will wait for user to stop submitting the tab). Otherwise closure is assumed when pressing the X, so if you keep submitting the tab may reappear at end of tab bar.
    no_nav = Literal[ImGuiWindowFlags_.no_nav_inputs] | Literal[ImGuiWindowFlags_.no_nav_focus]
    no_decoration = Literal[ImGuiWindowFlags_.no_title_bar] | Literal[ImGuiWindowFlags_.no_resize] | Literal[ImGuiWindowFlags_.no_scrollbar] | Literal[ImGuiWindowFlags_.no_collapse]
    no_inputs = Literal[ImGuiWindowFlags_.no_mouse_inputs] | Literal[ImGuiWindowFlags_.no_nav_inputs] | Literal[ImGuiWindowFlags_.no_nav_focus]

    # [Internal]
    nav_flattened = 1 << 23               # [BETA] On child window: allow gamepad/keyboard navigation to cross over parent border to this child or between sibling child windows.
    child_window = 1 << 24                # Don't use! For internal use by BeginChild()
    tooltip = 1 << 25                     # Don't use! For internal use by BeginTooltip()
    popup = 1 << 26                       # Don't use! For internal use by BeginPopup()
    modal = 1 << 27                       # Don't use! For internal use by BeginPopupModal()
    child_menu = 1 << 28                  # Don't use! For internal use by BeginMenu()
    #ImGuiWindowFlags_ResizeFromAnySide    = 1 << 17,  // [Obsolete] --> Set io.ConfigWindowsResizeFromEdges=True and make sure mouse cursors are supported by backend (io.BackendFlags & ImGuiBackendFlags_HasMouseCursors)

class ImGuiInputTextFlags_(Enum):    # imgui.h:981
    """ Flags for ImGui::InputText()"""
    none = 0
    chars_decimal = 1 << 0             # Allow 0123456789.+-*/
    chars_hexadecimal = 1 << 1         # Allow 0123456789ABCDEFabcdef
    chars_uppercase = 1 << 2           # Turn a..z into A..Z
    chars_no_blank = 1 << 3            # Filter out spaces, tabs
    auto_select_all = 1 << 4           # Select entire text when first taking mouse focus
    enter_returns_true = 1 << 5        # Return 'True' when Enter is pressed (as opposed to every time the value was modified). Consider looking at the IsItemDeactivatedAfterEdit() function.
    callback_completion = 1 << 6       # Callback on pressing TAB (for completion handling)
    callback_history = 1 << 7          # Callback on pressing Up/Down arrows (for history handling)
    callback_always = 1 << 8           # Callback on each iteration. User code may query cursor position, modify text buffer.
    callback_char_filter = 1 << 9      # Callback on character inputs to replace or discard them. Modify 'EventChar' to replace or discard, or return 1 in callback to discard.
    allow_tab_input = 1 << 10          # Pressing TAB input a '\t' character into the text field
    ctrl_enter_for_new_line = 1 << 11  # In multi-line mode, unfocus with Enter, add new line with Ctrl+Enter (default is opposite: unfocus with Ctrl+Enter, add line with Enter).
    no_horizontal_scroll = 1 << 12     # Disable following the cursor horizontally
    always_overwrite = 1 << 13         # Overwrite mode
    read_only = 1 << 14                # Read-only mode
    password = 1 << 15                 # Password mode, display all characters as '*'
    no_undo_redo = 1 << 16             # Disable undo/redo. Note that input text owns the text data while active, if you want to provide your own undo/redo stack you need e.g. to call ClearActiveID().
    chars_scientific = 1 << 17         # Allow 0123456789.+-*/eE (Scientific notation input)
    callback_resize = 1 << 18          # Callback on buffer capacity changes request (beyond 'buf_size' parameter value), allowing the string to grow. Notify when the string wants to be resized (for string types which hold a cache of their Size). You will be provided a new BufSize in the callback and NEED to honor it. (see misc/cpp/imgui_stdlib.h for an example of using this)
    callback_edit = 1 << 19
    # Callback on any edit (note that InputText() already returns True on edit, the callback is useful mainly to manipulate the underlying buffer while focus is active)

    # Obsolete names (will be removed soon)

class ImGuiTreeNodeFlags_(Enum):    # imgui.h:1012
    """ Flags for ImGui::TreeNodeEx(), ImGui::CollapsingHeader*()"""
    none = 0
    selected = 1 << 0                   # Draw as selected
    framed = 1 << 1                     # Draw frame with background (e.g. for CollapsingHeader)
    allow_item_overlap = 1 << 2         # Hit testing to allow subsequent widgets to overlap this one
    no_tree_push_on_open = 1 << 3       # Don't do a TreePush() when open (e.g. for CollapsingHeader) = no extra indent nor pushing on ID stack
    no_auto_open_on_log = 1 << 4        # Don't automatically and temporarily open node when Logging is active (by default logging will automatically open tree nodes)
    default_open = 1 << 5               # Default node to be open
    open_on_double_click = 1 << 6       # Need double-click to open node
    open_on_arrow = 1 << 7              # Only open when clicking on the arrow part. If ImGuiTreeNodeFlags_OpenOnDoubleClick is also set, single-click arrow or double-click all box to open.
    leaf = 1 << 8                       # No collapsing, no arrow (use as a convenience for leaf nodes).
    bullet = 1 << 9                     # Display a bullet instead of arrow
    frame_padding = 1 << 10             # Use FramePadding (even for an unframed text node) to vertically align text baseline to regular widget height. Equivalent to calling AlignTextToFramePadding().
    span_avail_width = 1 << 11          # Extend hit box to the right-most edge, even if not framed. This is not the default in order to allow adding other items on the same line. In the future we may refactor the hit system to be front-to-back, allowing natural overlaps and then this can become the default.
    span_full_width = 1 << 12           # Extend hit box to the left-most and right-most edges (bypass the indented area).
    nav_left_jumps_back_here = 1 << 13  # (WIP) Nav: left direction may move to this TreeNode() from any of its child (items submitted between TreeNode and TreePop)
    #ImGuiTreeNodeFlags_NoScrollOnOpen     = 1 << 14,  // FIXME: TODO: Disable automatic scroll on TreePop() if node got just open and contents is not visible
    collapsing_header = Literal[ImGuiTreeNodeFlags_.framed] | Literal[ImGuiTreeNodeFlags_.no_tree_push_on_open] | Literal[ImGuiTreeNodeFlags_.no_auto_open_on_log]

class ImGuiPopupFlags_(Enum):    # imgui.h:1041
    """ Flags for OpenPopup*(), BeginPopupContext*(), IsPopupOpen() functions.
     - To be backward compatible with older API which took an 'int mouse_button = 1' argument, we need to treat
       small flags values as a mouse button index, so we encode the mouse button in the first few bits of the flags.
       It is therefore guaranteed to be legal to pass a mouse button index in ImGuiPopupFlags.
     - For the same reason, we exceptionally default the ImGuiPopupFlags argument of BeginPopupContextXXX functions to 1 instead of 0.
       IMPORTANT: because the default parameter is 1 (==ImGuiPopupFlags_MouseButtonRight), if you rely on the default parameter
       and want to another another flag, you need to pass in the ImGuiPopupFlags_MouseButtonRight flag.
     - Multiple buttons currently cannot be combined/or-ed in those functions (we could allow it later).
    """
    none = 0
    mouse_button_left = 0                 # For BeginPopupContext*(): open on Left Mouse release. Guaranteed to always be == 0 (same as ImGuiMouseButton_Left)
    mouse_button_right = 1                # For BeginPopupContext*(): open on Right Mouse release. Guaranteed to always be == 1 (same as ImGuiMouseButton_Right)
    mouse_button_middle = 2               # For BeginPopupContext*(): open on Middle Mouse release. Guaranteed to always be == 2 (same as ImGuiMouseButton_Middle)
    mouse_button_mask_ = 0x1F
    mouse_button_default_ = 1
    no_open_over_existing_popup = 1 << 5  # For OpenPopup*(), BeginPopupContext*(): don't open if there's already a popup at the same level of the popup stack
    no_open_over_items = 1 << 6           # For BeginPopupContextWindow(): don't return True when hovering items, only when hovering empty space
    any_popup_id = 1 << 7                 # For IsPopupOpen(): ignore the ImGuiID parameter and test for any popup.
    any_popup_level = 1 << 8              # For IsPopupOpen(): search/test at any level of the popup stack (default test in the current level)
    any_popup = Literal[ImGuiPopupFlags_.any_popup_id] | Literal[ImGuiPopupFlags_.any_popup_level]

class ImGuiSelectableFlags_(Enum):    # imgui.h:1057
    """ Flags for ImGui::Selectable()"""
    none = 0
    dont_close_popups = 1 << 0   # Clicking this don't close parent popup window
    span_all_columns = 1 << 1    # Selectable frame can span all columns (text will still fit in current column)
    allow_double_click = 1 << 2  # Generate press events on double clicks too
    disabled = 1 << 3            # Cannot be selected, display grayed out text
    allow_item_overlap = 1 << 4  # (WIP) Hit testing to allow subsequent widgets to overlap this one

class ImGuiComboFlags_(Enum):    # imgui.h:1068
    """ Flags for ImGui::BeginCombo()"""
    none = 0
    popup_align_left = 1 << 0  # Align the popup toward the left by default
    height_small = 1 << 1      # Max ~4 items visible. Tip: If you want your combo popup to be a specific size you can use SetNextWindowSizeConstraints() prior to calling BeginCombo()
    height_regular = 1 << 2    # Max ~8 items visible (default)
    height_large = 1 << 3      # Max ~20 items visible
    height_largest = 1 << 4    # As many fitting items as possible
    no_arrow_button = 1 << 5   # Display on the preview box without the square arrow button
    no_preview = 1 << 6        # Display only a square arrow button
    height_mask_ = Literal[ImGuiComboFlags_.height_small] | Literal[ImGuiComboFlags_.height_regular] | Literal[ImGuiComboFlags_.height_large] | Literal[ImGuiComboFlags_.height_largest]

class ImGuiTabBarFlags_(Enum):    # imgui.h:1082
    """ Flags for ImGui::BeginTabBar()"""
    none = 0
    reorderable = 1 << 0                        # Allow manually dragging tabs to re-order them + New tabs are appended at the end of list
    auto_select_new_tabs = 1 << 1               # Automatically select new tabs when they appear
    tab_list_popup_button = 1 << 2              # Disable buttons to open the tab list popup
    no_close_with_middle_mouse_button = 1 << 3  # Disable behavior of closing tabs (that are submitted with p_open != None) with middle mouse button. You can still repro this behavior on user's side with if (IsItemHovered() && IsMouseClicked(2)) *p_open = False.
    no_tab_list_scrolling_buttons = 1 << 4      # Disable scrolling buttons (apply when fitting policy is ImGuiTabBarFlags_FittingPolicyScroll)
    no_tooltip = 1 << 5                         # Disable tooltips when hovering a tab
    fitting_policy_resize_down = 1 << 6         # Resize tabs when they don't fit
    fitting_policy_scroll = 1 << 7              # Add scroll buttons when tabs don't fit
    fitting_policy_mask_ = Literal[ImGuiTabBarFlags_.fitting_policy_resize_down] | Literal[ImGuiTabBarFlags_.fitting_policy_scroll]
    fitting_policy_default_ = Literal[ImGuiTabBarFlags_.fitting_policy_resize_down]

class ImGuiTabItemFlags_(Enum):    # imgui.h:1098
    """ Flags for ImGui::BeginTabItem()"""
    none = 0
    unsaved_document = 1 << 0                   # Display a dot next to the title + tab is selected when clicking the X + closure is not assumed (will wait for user to stop submitting the tab). Otherwise closure is assumed when pressing the X, so if you keep submitting the tab may reappear at end of tab bar.
    set_selected = 1 << 1                       # Trigger flag to programmatically make the tab selected when calling BeginTabItem()
    no_close_with_middle_mouse_button = 1 << 2  # Disable behavior of closing tabs (that are submitted with p_open != None) with middle mouse button. You can still repro this behavior on user's side with if (IsItemHovered() && IsMouseClicked(2)) *p_open = False.
    no_push_id = 1 << 3                         # Don't call PushID(tab->ID)/PopID() on BeginTabItem()/EndTabItem()
    no_tooltip = 1 << 4                         # Disable tooltip for the given tab
    no_reorder = 1 << 5                         # Disable reordering this tab or having another tab cross over this tab
    leading = 1 << 6                            # Enforce the tab position to the left of the tab bar (after the tab list popup button)
    trailing = 1 << 7                           # Enforce the tab position to the right of the tab bar (before the scrolling buttons)

class ImGuiTableFlags_(Enum):    # imgui.h:1133
    """ Flags for ImGui::BeginTable()
     - Important! Sizing policies have complex and subtle side effects, much more so than you would expect.
       Read comments/demos carefully + experiment with live demos to get acquainted with them.
     - The DEFAULT sizing policies are:
        - Default to ImGuiTableFlags_SizingFixedFit    if ScrollX is on, or if host window has ImGuiWindowFlags_AlwaysAutoResize.
        - Default to ImGuiTableFlags_SizingStretchSame if ScrollX is off.
     - When ScrollX is off:
        - Table defaults to ImGuiTableFlags_SizingStretchSame -> all Columns defaults to ImGuiTableColumnFlags_WidthStretch with same weight.
        - Columns sizing policy allowed: Stretch (default), Fixed/Auto.
        - Fixed Columns (if any) will generally obtain their requested width (unless the table cannot fit them all).
        - Stretch Columns will share the remaining width according to their respective weight.
        - Mixed Fixed/Stretch columns is possible but has various side-effects on resizing behaviors.
          The typical use of mixing sizing policies is: any number of LEADING Fixed columns, followed by one or two TRAILING Stretch columns.
          (this is because the visible order of columns have subtle but necessary effects on how they react to manual resizing).
     - When ScrollX is on:
        - Table defaults to ImGuiTableFlags_SizingFixedFit -> all Columns defaults to ImGuiTableColumnFlags_WidthFixed
        - Columns sizing policy allowed: Fixed/Auto mostly.
        - Fixed Columns can be enlarged as needed. Table will show an horizontal scrollbar if needed.
        - When using auto-resizing (non-resizable) fixed columns, querying the content width to use item right-alignment e.g. SetNextItemWidth(-FLT_MIN) doesn't make sense, would create a feedback loop.
        - Using Stretch columns OFTEN DOES NOT MAKE SENSE if ScrollX is on, UNLESS you have specified a value for 'inner_width' in BeginTable().
          If you specify a value for 'inner_width' then effectively the scrolling space is known and Stretch or mixed Fixed/Stretch columns become meaningful again.
     - Read on documentation at the top of imgui_tables.cpp for details.
    """
    # Features
    none = 0
    resizable = 1 << 0                                                                                     # Enable resizing columns.
    reorderable = 1 << 1                                                                                   # Enable reordering columns in header row (need calling TableSetupColumn() + TableHeadersRow() to display headers)
    hideable = 1 << 2                                                                                      # Enable hiding/disabling columns in context menu.
    sortable = 1 << 3                                                                                      # Enable sorting. Call TableGetSortSpecs() to obtain sort specs. Also see ImGuiTableFlags_SortMulti and ImGuiTableFlags_SortTristate.
    no_saved_settings = 1 << 4                                                                             # Disable persisting columns order, width and sort settings in the .ini file.
    context_menu_in_body = 1 << 5                                                                          # Right-click on columns body/contents will display table context menu. By default it is available in TableHeadersRow().
    # Decorations
    row_bg = 1 << 6                                                                                        # Set each RowBg color with ImGuiCol_TableRowBg or ImGuiCol_TableRowBgAlt (equivalent of calling TableSetBgColor with ImGuiTableBgFlags_RowBg0 on each row manually)
    borders_inner_h = 1 << 7                                                                               # Draw horizontal borders between rows.
    borders_outer_h = 1 << 8                                                                               # Draw horizontal borders at the top and bottom.
    borders_inner_v = 1 << 9                                                                               # Draw vertical borders between columns.
    borders_outer_v = 1 << 10                                                                              # Draw vertical borders on the left and right sides.
    borders_h = Literal[ImGuiTableFlags_.borders_inner_h] | Literal[ImGuiTableFlags_.borders_outer_h]      # Draw horizontal borders.
    borders_v = Literal[ImGuiTableFlags_.borders_inner_v] | Literal[ImGuiTableFlags_.borders_outer_v]      # Draw vertical borders.
    borders_inner = Literal[ImGuiTableFlags_.borders_inner_v] | Literal[ImGuiTableFlags_.borders_inner_h]  # Draw inner borders.
    borders_outer = Literal[ImGuiTableFlags_.borders_outer_v] | Literal[ImGuiTableFlags_.borders_outer_h]  # Draw outer borders.
    borders = Literal[ImGuiTableFlags_.borders_inner] | Literal[ImGuiTableFlags_.borders_outer]            # Draw all borders.
    no_borders_in_body = 1 << 11                                                                           # [ALPHA] Disable vertical borders in columns Body (borders will always appears in Headers). -> May move to style
    no_borders_in_body_until_resize = 1 << 12                                                              # [ALPHA] Disable vertical borders in columns Body until hovered for resize (borders will always appears in Headers). -> May move to style
    # Sizing Policy (read above for defaults)
    sizing_fixed_fit = 1 << 13                                                                             # Columns default to _WidthFixed or _WidthAuto (if resizable or not resizable), matching contents width.
    sizing_fixed_same = 2 << 13                                                                            # Columns default to _WidthFixed or _WidthAuto (if resizable or not resizable), matching the maximum contents width of all columns. Implicitly enable ImGuiTableFlags_NoKeepColumnsVisible.
    sizing_stretch_prop = 3 << 13                                                                          # Columns default to _WidthStretch with default weights proportional to each columns contents widths.
    sizing_stretch_same = 4 << 13                                                                          # Columns default to _WidthStretch with default weights all equal, unless overridden by TableSetupColumn().
    # Sizing Extra Options
    no_host_extend_x = 1 << 16                                                                             # Make outer width auto-fit to columns, overriding outer_size.x value. Only available when ScrollX/ScrollY are disabled and Stretch columns are not used.
    no_host_extend_y = 1 << 17                                                                             # Make outer height stop exactly at outer_size.y (prevent auto-extending table past the limit). Only available when ScrollX/ScrollY are disabled. Data below the limit will be clipped and not visible.
    no_keep_columns_visible = 1 << 18                                                                      # Disable keeping column always minimally visible when ScrollX is off and table gets too small. Not recommended if columns are resizable.
    precise_widths = 1 << 19                                                                               # Disable distributing remainder width to stretched columns (width allocation on a 100-wide table with 3 columns: Without this flag: 33,33,34. With this flag: 33,33,33). With larger number of columns, resizing will appear to be less smooth.
    # Clipping
    no_clip = 1 << 20                                                                                      # Disable clipping rectangle for every individual columns (reduce draw command count, items will be able to overflow into other columns). Generally incompatible with TableSetupScrollFreeze().
    # Padding
    pad_outer_x = 1 << 21                                                                                  # Default if BordersOuterV is on. Enable outer-most padding. Generally desirable if you have headers.
    no_pad_outer_x = 1 << 22                                                                               # Default if BordersOuterV is off. Disable outer-most padding.
    no_pad_inner_x = 1 << 23                                                                               # Disable inner padding between columns (double inner padding if BordersOuterV is on, single inner padding if BordersOuterV is off).
    # Scrolling
    scroll_x = 1 << 24                                                                                     # Enable horizontal scrolling. Require 'outer_size' parameter of BeginTable() to specify the container size. Changes default sizing policy. Because this create a child window, ScrollY is currently generally recommended when using ScrollX.
    scroll_y = 1 << 25                                                                                     # Enable vertical scrolling. Require 'outer_size' parameter of BeginTable() to specify the container size.
    # Sorting
    sort_multi = 1 << 26                                                                                   # Hold shift when clicking headers to sort on multiple column. TableGetSortSpecs() may return specs where (SpecsCount > 1).
    sort_tristate = 1 << 27                                                                                # Allow no sorting, disable default sorting. TableGetSortSpecs() may return specs where (SpecsCount == 0).

    # [Internal] Combinations and masks
    sizing_mask_ = Literal[ImGuiTableFlags_.sizing_fixed_fit] | Literal[ImGuiTableFlags_.sizing_fixed_same] | Literal[ImGuiTableFlags_.sizing_stretch_prop] | Literal[ImGuiTableFlags_.sizing_stretch_same]

    # Obsolete names (will be removed soon)

class ImGuiTableColumnFlags_(Enum):    # imgui.h:1190
    """ Flags for ImGui::TableSetupColumn()"""
    # Input configuration flags
    none = 0
    disabled = 1 << 0                 # Overriding/master disable flag: hide column, won't show in context menu (unlike calling TableSetColumnEnabled() which manipulates the user accessible state)
    default_hide = 1 << 1             # Default as a hidden/disabled column.
    default_sort = 1 << 2             # Default as a sorting column.
    width_stretch = 1 << 3            # Column will stretch. Preferable with horizontal scrolling disabled (default if table sizing policy is _SizingStretchSame or _SizingStretchProp).
    width_fixed = 1 << 4              # Column will not stretch. Preferable with horizontal scrolling enabled (default if table sizing policy is _SizingFixedFit and table is resizable).
    no_resize = 1 << 5                # Disable manual resizing.
    no_reorder = 1 << 6               # Disable manual reordering this column, this will also prevent other columns from crossing over this column.
    no_hide = 1 << 7                  # Disable ability to hide/disable this column.
    no_clip = 1 << 8                  # Disable clipping for this column (all NoClip columns will render in a same draw command).
    no_sort = 1 << 9                  # Disable ability to sort on this field (even if ImGuiTableFlags_Sortable is set on the table).
    no_sort_ascending = 1 << 10       # Disable ability to sort in the ascending direction.
    no_sort_descending = 1 << 11      # Disable ability to sort in the descending direction.
    no_header_label = 1 << 12         # TableHeadersRow() will not submit label for this column. Convenient for some small columns. Name will still appear in context menu.
    no_header_width = 1 << 13         # Disable header text width contribution to automatic column width.
    prefer_sort_ascending = 1 << 14   # Make the initial sort direction Ascending when first sorting on this column (default).
    prefer_sort_descending = 1 << 15  # Make the initial sort direction Descending when first sorting on this column.
    indent_enable = 1 << 16           # Use current Indent value when entering cell (default for column 0).
    indent_disable = 1 << 17          # Ignore current Indent value when entering cell (default for columns > 0). Indentation changes _within_ the cell will still be honored.

    # Output status flags, read-only via TableGetColumnFlags()
    is_enabled = 1 << 24              # Status: is enabled == not hidden by user/api (referred to as "Hide" in _DefaultHide and _NoHide) flags.
    is_visible = 1 << 25              # Status: is visible == is enabled AND not clipped by scrolling.
    is_sorted = 1 << 26               # Status: is currently part of the sort specs
    is_hovered = 1 << 27              # Status: is hovered by mouse

    # [Internal] Combinations and masks
    width_mask_ = Literal[ImGuiTableColumnFlags_.width_stretch] | Literal[ImGuiTableColumnFlags_.width_fixed]
    indent_mask_ = Literal[ImGuiTableColumnFlags_.indent_enable] | Literal[ImGuiTableColumnFlags_.indent_disable]
    status_mask_ = Literal[ImGuiTableColumnFlags_.is_enabled] | Literal[ImGuiTableColumnFlags_.is_visible] | Literal[ImGuiTableColumnFlags_.is_sorted] | Literal[ImGuiTableColumnFlags_.is_hovered]
    no_direct_resize_ = 1 << 30
    # [Internal] Disable user resizing this column directly (it may however we resized indirectly from its left edge)

    # Obsolete names (will be removed soon)

class ImGuiTableRowFlags_(Enum):    # imgui.h:1232
    """ Flags for ImGui::TableNextRow()"""
    none = 0
    headers = 1 << 0  # Identify header row (set default background color + width of its contents accounted differently for auto column width)

class ImGuiTableBgTarget_(Enum):    # imgui.h:1247
    """ Enum for ImGui::TableSetBgColor()
     Background colors are rendering in 3 layers:
      - Layer 0: draw with RowBg0 color if set, otherwise draw with ColumnBg0 if set.
      - Layer 1: draw with RowBg1 color if set, otherwise draw with ColumnBg1 if set.
      - Layer 2: draw with CellBg color if set.
     The purpose of the two row/columns layers is to let you decide if a background color changes should override or blend with the existing color.
     When using ImGuiTableFlags_RowBg on the table, each row has the RowBg0 color automatically set for odd/even rows.
     If you set the color of RowBg0 target, your color will override the existing RowBg0 color.
     If you set the color of RowBg1 or ColumnBg1 target, your color will blend over the RowBg0 color.
    """
    none = 0
    row_bg0 = 1  # Set row background color 0 (generally used for background, automatically set when ImGuiTableFlags_RowBg is used)
    row_bg1 = 2  # Set row background color 1 (generally used for selection marking)
    cell_bg = 3  # Set cell background color (top-most color)

class ImGuiFocusedFlags_(Enum):    # imgui.h:1256
    """ Flags for ImGui::IsWindowFocused()"""
    none = 0
    child_windows = 1 << 0       # Return True if any children of the window is focused
    root_window = 1 << 1         # Test from root window (top most parent of the current hierarchy)
    any_window = 1 << 2          # Return True if any window is focused. Important: If you are trying to tell how to dispatch your low-level inputs, do NOT use this. Use 'io.WantCaptureMouse' instead! Please read the FAQ!
    no_popup_hierarchy = 1 << 3  # Do not consider popup hierarchy (do not treat popup emitter as parent of popup) (when used with _ChildWindows or _RootWindow)
    #ImGuiFocusedFlags_DockHierarchy               = 1 << 4,   // Consider docking hierarchy (treat dockspace host as parent of docked window) (when used with _ChildWindows or _RootWindow)
    root_and_child_windows = Literal[ImGuiFocusedFlags_.root_window] | Literal[ImGuiFocusedFlags_.child_windows]

class ImGuiHoveredFlags_(Enum):    # imgui.h:1270
    """ Flags for ImGui::IsItemHovered(), ImGui::IsWindowHovered()
     Note: if you are trying to check whether your mouse should be dispatched to Dear ImGui or to your app, you should use 'io.WantCaptureMouse' instead! Please read the FAQ!
     Note: windows with the ImGuiWindowFlags_NoInputs flag are ignored by IsWindowHovered() calls.
    """
    none = 0                                    # Return True if directly over the item/window, not obstructed by another window, not obstructed by an active popup or modal blocking inputs under them.
    child_windows = 1 << 0                      # IsWindowHovered() only: Return True if any children of the window is hovered
    root_window = 1 << 1                        # IsWindowHovered() only: Test from root window (top most parent of the current hierarchy)
    any_window = 1 << 2                         # IsWindowHovered() only: Return True if any window is hovered
    no_popup_hierarchy = 1 << 3                 # IsWindowHovered() only: Do not consider popup hierarchy (do not treat popup emitter as parent of popup) (when used with _ChildWindows or _RootWindow)
    #ImGuiHoveredFlags_DockHierarchy               = 1 << 4,   // IsWindowHovered() only: Consider docking hierarchy (treat dockspace host as parent of docked window) (when used with _ChildWindows or _RootWindow)
    allow_when_blocked_by_popup = 1 << 5        # Return True even if a popup window is normally blocking access to this item/window
    #ImGuiHoveredFlags_AllowWhenBlockedByModal     = 1 << 6,   // Return True even if a modal popup window is normally blocking access to this item/window. FIXME-TODO: Unavailable yet.
    allow_when_blocked_by_active_item = 1 << 7  # Return True even if an active item is blocking access to this item/window. Useful for Drag and Drop patterns.
    allow_when_overlapped = 1 << 8              # IsItemHovered() only: Return True even if the position is obstructed or overlapped by another window
    allow_when_disabled = 1 << 9                # IsItemHovered() only: Return True even if the item is disabled
    no_nav_override = 1 << 10                   # Disable using gamepad/keyboard navigation state when active, always query mouse.
    rect_only = Literal[ImGuiHoveredFlags_.allow_when_blocked_by_popup] | Literal[ImGuiHoveredFlags_.allow_when_blocked_by_active_item] | Literal[ImGuiHoveredFlags_.allow_when_overlapped]
    root_and_child_windows = Literal[ImGuiHoveredFlags_.root_window] | Literal[ImGuiHoveredFlags_.child_windows]

class ImGuiDragDropFlags_(Enum):    # imgui.h:1289
    """ Flags for ImGui::BeginDragDropSource(), ImGui::AcceptDragDropPayload()"""
    none = 0
    # BeginDragDropSource() flags
    source_no_preview_tooltip = 1 << 0                                                                                                 # By default, a successful call to BeginDragDropSource opens a tooltip so you can display a preview or description of the source contents. This flag disable this behavior.
    source_no_disable_hover = 1 << 1                                                                                                   # By default, when dragging we clear data so that IsItemHovered() will return False, to avoid subsequent user code submitting tooltips. This flag disable this behavior so you can still call IsItemHovered() on the source item.
    source_no_hold_to_open_others = 1 << 2                                                                                             # Disable the behavior that allows to open tree nodes and collapsing header by holding over them while dragging a source item.
    source_allow_null_id = 1 << 3                                                                                                      # Allow items such as Text(), Image() that have no unique identifier to be used as drag source, by manufacturing a temporary identifier based on their window-relative position. This is extremely unusual within the dear imgui ecosystem and so we made it explicit.
    source_extern = 1 << 4                                                                                                             # External source (from outside of dear imgui), won't attempt to read current item/window info. Will always return True. Only one Extern source can be active simultaneously.
    source_auto_expire_payload = 1 << 5                                                                                                # Automatically expire the payload if the source cease to be submitted (otherwise payloads are persisting while being dragged)
    # AcceptDragDropPayload() flags
    accept_before_delivery = 1 << 10                                                                                                   # AcceptDragDropPayload() will returns True even before the mouse button is released. You can then call IsDelivery() to test if the payload needs to be delivered.
    accept_no_draw_default_rect = 1 << 11                                                                                              # Do not draw the default highlight rectangle when hovering over target.
    accept_no_preview_tooltip = 1 << 12                                                                                                # Request hiding the BeginDragDropSource tooltip from the BeginDragDropTarget site.
    accept_peek_only = Literal[ImGuiDragDropFlags_.accept_before_delivery] | Literal[ImGuiDragDropFlags_.accept_no_draw_default_rect]  # For peeking ahead and inspecting the payload before delivery.

# Standard Drag and Drop payload types. You can define you own payload types using short strings. Types starting with '_' are defined by Dear ImGui.

class ImGuiDataType_(Enum):    # imgui.h:1311
    """ A primary data type"""
    s8 = 0      # signed char / char (with sensible compilers)
    u8 = 1      # unsigned char
    s16 = 2     # short
    u16 = 3     # unsigned short
    s32 = 4     # int
    u32 = 5     # unsigned int
    s64 = 6     # long long / __int64
    u64 = 7     # unsigned long long / unsigned __int64
    float = 8   # float
    double = 9  # double
    count = 10

class ImGuiDir_(Enum):    # imgui.h:1327
    """ A cardinal direction"""
    none = -1
    left = 0
    right = 1
    up = 2
    down = 3
    count = 4

class ImGuiSortDirection_(Enum):    # imgui.h:1338
    """ A sorting direction"""
    none = 0
    ascending = 1   # Ascending = 0->9, A->Z etc.
    descending = 2  # Descending = 9->0, Z->A etc.

class ImGuiKey_(Enum):    # imgui.h:1347
    """ Keys value 0 to 511 are left unused as legacy native/opaque key values (< 1.87)
     Keys value >= 512 are named keys (>= 1.87)
    """
    # Keyboard
    none = 0
    tab = 512                    # == ImGuiKey_NamedKey_BEGIN
    left_arrow = 513
    right_arrow = 514
    up_arrow = 515
    down_arrow = 516
    page_up = 517
    page_down = 518
    home = 519
    end = 520
    insert = 521
    delete = 522
    backspace = 523
    space = 524
    enter = 525
    escape = 526
    left_ctrl = 527
    left_shift = 528
    left_alt = 529
    left_super = 530
    right_ctrl = 531
    right_shift = 532
    right_alt = 533
    right_super = 534
    menu = 535
    _0 = 536
    _1 = 537
    _2 = 538
    _3 = 539
    _4 = 540
    _5 = 541
    _6 = 542
    _7 = 543
    _8 = 544
    _9 = 545
    a = 546
    b = 547
    c = 548
    d = 549
    e = 550
    f = 551
    g = 552
    h = 553
    i = 554
    j = 555
    k = 556
    l = 557
    m = 558
    n = 559
    o = 560
    p = 561
    q = 562
    r = 563
    s = 564
    t = 565
    u = 566
    v = 567
    w = 568
    x = 569
    y = 570
    z = 571
    f1 = 572
    f2 = 573
    f3 = 574
    f4 = 575
    f5 = 576
    f6 = 577
    f7 = 578
    f8 = 579
    f9 = 580
    f10 = 581
    f11 = 582
    f12 = 583
    apostrophe = 584             # '
    comma = 585                  # ,
    minus = 586                  # -
    period = 587                 # .
    slash = 588                  # /
    semicolon = 589              # ;
    equal = 590                  # =
    left_bracket = 591           # [
    backslash = 592              # \ (this text inhibit multiline comment caused by backslash)
    right_bracket = 593          # ]
    grave_accent = 594           # `
    caps_lock = 595
    scroll_lock = 596
    num_lock = 597
    print_screen = 598
    pause = 599
    keypad0 = 600
    keypad1 = 601
    keypad2 = 602
    keypad3 = 603
    keypad4 = 604
    keypad5 = 605
    keypad6 = 606
    keypad7 = 607
    keypad8 = 608
    keypad9 = 609
    keypad_decimal = 610
    keypad_divide = 611
    keypad_multiply = 612
    keypad_subtract = 613
    keypad_add = 614
    keypad_enter = 615
    keypad_equal = 616

    # Gamepad (some of those are analog values, 0.0 to 1.0)                              // NAVIGATION action
    gamepad_start = 617          # Menu (Xbox)          + (Switch)   Start/Options (PS) // --
    gamepad_back = 618           # View (Xbox)          - (Switch)   Share (PS)         // --
    gamepad_face_up = 619        # Y (Xbox)             X (Switch)   Triangle (PS)      // -> ImGuiNavInput_Input
    gamepad_face_down = 620      # A (Xbox)             B (Switch)   Cross (PS)         // -> ImGuiNavInput_Activate
    gamepad_face_left = 621      # X (Xbox)             Y (Switch)   Square (PS)        // -> ImGuiNavInput_Menu
    gamepad_face_right = 622     # B (Xbox)             A (Switch)   Circle (PS)        // -> ImGuiNavInput_Cancel
    gamepad_dpad_up = 623        # D-pad Up                                             // -> ImGuiNavInput_DpadUp
    gamepad_dpad_down = 624      # D-pad Down                                           // -> ImGuiNavInput_DpadDown
    gamepad_dpad_left = 625      # D-pad Left                                           // -> ImGuiNavInput_DpadLeft
    gamepad_dpad_right = 626     # D-pad Right                                          // -> ImGuiNavInput_DpadRight
    gamepad_l1 = 627             # L Bumper (Xbox)      L (Switch)   L1 (PS)            // -> ImGuiNavInput_FocusPrev + ImGuiNavInput_TweakSlow
    gamepad_r1 = 628             # R Bumper (Xbox)      R (Switch)   R1 (PS)            // -> ImGuiNavInput_FocusNext + ImGuiNavInput_TweakFast
    gamepad_l2 = 629             # L Trigger (Xbox)     ZL (Switch)  L2 (PS) [Analog]
    gamepad_r2 = 630             # R Trigger (Xbox)     ZR (Switch)  R2 (PS) [Analog]
    gamepad_l3 = 631             # L Thumbstick (Xbox)  L3 (Switch)  L3 (PS)
    gamepad_r3 = 632             # R Thumbstick (Xbox)  R3 (Switch)  R3 (PS)
    gamepad_l_stick_up = 633     # [Analog]                                             // -> ImGuiNavInput_LStickUp
    gamepad_l_stick_down = 634   # [Analog]                                             // -> ImGuiNavInput_LStickDown
    gamepad_l_stick_left = 635   # [Analog]                                             // -> ImGuiNavInput_LStickLeft
    gamepad_l_stick_right = 636  # [Analog]                                             // -> ImGuiNavInput_LStickRight
    gamepad_r_stick_up = 637     # [Analog]
    gamepad_r_stick_down = 638   # [Analog]
    gamepad_r_stick_left = 639   # [Analog]
    gamepad_r_stick_right = 640  # [Analog]

    # Keyboard Modifiers (explicitly submitted by backend via AddKeyEvent() calls)
    # - This is mirroring the data also written to io.KeyCtrl, io.KeyShift, io.KeyAlt, io.KeySuper, in a format allowing
    #   them to be accessed via standard key API, allowing calls such as IsKeyPressed(), IsKeyReleased(), querying duration etc.
    # - Code polling every keys (e.g. an interface to detect a key press for input mapping) might want to ignore those
    #   and prefer using the real keys (e.g. ImGuiKey_LeftCtrl, ImGuiKey_RightCtrl instead of ImGuiKey_ModCtrl).
    # - In theory the value of keyboard modifiers should be roughly equivalent to a logical or of the equivalent left/right keys.
    #   In practice: it's complicated; mods are often provided from different sources. Keyboard layout, IME, sticky keys and
    #   backends tend to interfere and break that equivalence. The safer decision is to relay that ambiguity down to the end-user...
    mod_ctrl = 641
    mod_shift = 642
    mod_alt = 643
    mod_super = 644

    # End of list
    count = 645                  # No valid ImGuiKey is ever greater than this value

    # [Internal] Prior to 1.87 we required user to fill io.KeysDown[512] using their own native index + a io.KeyMap[] array.
    # We are ditching this method but keeping a legacy path for user code doing e.g. IsKeyPressed(MY_NATIVE_KEY_CODE)
    named_key_begin = 512
    named_key_end = Literal[ImGuiKey_.count]
    named_key_count = Literal[ImGuiKey_.named_key_end] - Literal[ImGuiKey_.named_key_begin]


class ImGuiModFlags_(Enum):    # imgui.h:1459
    """ Helper "flags" version of key-mods to store and compare multiple key-mods easily. Sometimes used for storage (e.g. io.KeyMods) but otherwise not much used in public API."""
    none = 0
    ctrl = 1 << 0
    shift = 1 << 1
    alt = 1 << 2    # Menu
    super = 1 << 3  # Cmd/Super/Windows key

class ImGuiNavInput_(Enum):    # imgui.h:1473
    """ Gamepad/Keyboard navigation
     Since >= 1.87 backends you generally don't need to care about this enum since io.NavInputs[] is setup automatically. This might become private/internal some day.
     Keyboard: Set io.ConfigFlags |= ImGuiConfigFlags_NavEnableKeyboard to enable. NewFrame() will automatically fill io.NavInputs[] based on your io.AddKeyEvent() calls.
     Gamepad:  Set io.ConfigFlags |= ImGuiConfigFlags_NavEnableGamepad to enable. Backend: set ImGuiBackendFlags_HasGamepad and fill the io.NavInputs[] fields before calling NewFrame(). Note that io.NavInputs[] is cleared by EndFrame().
     Read instructions in imgui.cpp for more details. Download PNG/PSD at http://dearimgui.org/controls_sheets.
    """
    # Gamepad Mapping
    activate = 0      # Activate / Open / Toggle / Tweak value       // e.g. Cross  (PS4), A (Xbox), A (Switch), Space (Keyboard)
    cancel = 1        # Cancel / Close / Exit                        // e.g. Circle (PS4), B (Xbox), B (Switch), Escape (Keyboard)
    input = 2         # Text input / On-Screen keyboard              // e.g. Triang.(PS4), Y (Xbox), X (Switch), Return (Keyboard)
    menu = 3          # Tap: Toggle menu / Hold: Focus, Move, Resize // e.g. Square (PS4), X (Xbox), Y (Switch), Alt (Keyboard)
    dpad_left = 4     # Move / Tweak / Resize window (w/ PadMenu)    // e.g. D-pad Left/Right/Up/Down (Gamepads), Arrow keys (Keyboard)
    dpad_right = 5
    dpad_up = 6
    dpad_down = 7
    l_stick_left = 8  # Scroll / Move window (w/ PadMenu)            // e.g. Left Analog Stick Left/Right/Up/Down
    l_stick_right = 9
    l_stick_up = 10
    l_stick_down = 11
    focus_prev = 12   # Focus Next window (w/ PadMenu)               // e.g. L1 or L2 (PS4), LB or LT (Xbox), L or ZL (Switch)
    focus_next = 13   # Focus Prev window (w/ PadMenu)               // e.g. R1 or R2 (PS4), RB or RT (Xbox), R or ZL (Switch)
    tweak_slow = 14   # Slower tweaks                                // e.g. L1 or L2 (PS4), LB or LT (Xbox), L or ZL (Switch)
    tweak_fast = 15   # Faster tweaks                                // e.g. R1 or R2 (PS4), RB or RT (Xbox), R or ZL (Switch)

    # [Internal] Don't use directly! This is used internally to differentiate keyboard from gamepad inputs for behaviors that require to differentiate them.
    # Keyboard behavior that have no corresponding gamepad mapping (e.g. CTRL+TAB) will be directly reading from keyboard keys instead of io.NavInputs[].
    key_left_ = 16    # Move left                                    // = Arrow keys
    key_right_ = 17   # Move right
    key_up_ = 18      # Move up
    key_down_ = 19    # Move down
    count = 20

class ImGuiConfigFlags_(Enum):    # imgui.h:1503
    """ Configuration flags stored in io.ConfigFlags. Set by user/application."""
    none = 0
    nav_enable_keyboard = 1 << 0       # Master keyboard navigation enable flag. NewFrame() will automatically fill io.NavInputs[] based on io.AddKeyEvent() calls
    nav_enable_gamepad = 1 << 1        # Master gamepad navigation enable flag. This is mostly to instruct your imgui backend to fill io.NavInputs[]. Backend also needs to set ImGuiBackendFlags_HasGamepad.
    nav_enable_set_mouse_pos = 1 << 2  # Instruct navigation to move the mouse cursor. May be useful on TV/console systems where moving a virtual mouse is awkward. Will update io.MousePos and set io.WantSetMousePos=True. If enabled you MUST honor io.WantSetMousePos requests in your backend, otherwise ImGui will react as if the mouse is jumping around back and forth.
    nav_no_capture_keyboard = 1 << 3   # Instruct navigation to not set the io.WantCaptureKeyboard flag when io.NavActive is set.
    no_mouse = 1 << 4                  # Instruct imgui to clear mouse position/buttons in NewFrame(). This allows ignoring the mouse information set by the backend.
    no_mouse_cursor_change = 1 << 5    # Instruct backend to not alter mouse cursor shape and visibility. Use if the backend cursor changes are interfering with yours and you don't want to use SetMouseCursor() to change mouse cursor. You may want to honor requests from imgui by reading GetMouseCursor() yourself instead.

    # User storage (to allow your backend/engine to communicate to code that may be shared between multiple projects. Those flags are NOT used by core Dear ImGui)
    is_srgb = 1 << 20                  # Application is SRGB-aware.
    is_touch_screen = 1 << 21          # Application is using a touch screen instead of a mouse.

class ImGuiBackendFlags_(Enum):    # imgui.h:1519
    """ Backend capabilities flags stored in io.BackendFlags. Set by imgui_impl_xxx or custom backend."""
    none = 0
    has_gamepad = 1 << 0              # Backend Platform supports gamepad and currently has one connected.
    has_mouse_cursors = 1 << 1        # Backend Platform supports honoring GetMouseCursor() value to change the OS cursor shape.
    has_set_mouse_pos = 1 << 2        # Backend Platform supports io.WantSetMousePos requests to reposition the OS mouse position (only used if ImGuiConfigFlags_NavEnableSetMousePos is set).
    renderer_has_vtx_offset = 1 << 3  # Backend Renderer supports ImDrawCmd::VtxOffset. This enables output of large meshes (64K+ vertices) while still using 16-bit indices.

class ImGuiCol_(Enum):    # imgui.h:1529
    """ Enumeration for PushStyleColor() / PopStyleColor()"""
    text = 0
    text_disabled = 1
    window_bg = 2                 # Background of normal windows
    child_bg = 3                  # Background of child windows
    popup_bg = 4                  # Background of popups, menus, tooltips windows
    border = 5
    border_shadow = 6
    frame_bg = 7                  # Background of checkbox, radio button, plot, slider, text input
    frame_bg_hovered = 8
    frame_bg_active = 9
    title_bg = 10
    title_bg_active = 11
    title_bg_collapsed = 12
    menu_bar_bg = 13
    scrollbar_bg = 14
    scrollbar_grab = 15
    scrollbar_grab_hovered = 16
    scrollbar_grab_active = 17
    check_mark = 18
    slider_grab = 19
    slider_grab_active = 20
    button = 21
    button_hovered = 22
    button_active = 23
    header = 24                   # Header* colors are used for CollapsingHeader, TreeNode, Selectable, MenuItem
    header_hovered = 25
    header_active = 26
    separator = 27
    separator_hovered = 28
    separator_active = 29
    resize_grip = 30              # Resize grip in lower-right and lower-left corners of windows.
    resize_grip_hovered = 31
    resize_grip_active = 32
    tab = 33                      # TabItem in a TabBar
    tab_hovered = 34
    tab_active = 35
    tab_unfocused = 36
    tab_unfocused_active = 37
    plot_lines = 38
    plot_lines_hovered = 39
    plot_histogram = 40
    plot_histogram_hovered = 41
    table_header_bg = 42          # Table header background
    table_border_strong = 43      # Table outer and header borders (prefer using Alpha=1.0 here)
    table_border_light = 44       # Table inner borders (prefer using Alpha=1.0 here)
    table_row_bg = 45             # Table row background (even rows)
    table_row_bg_alt = 46         # Table row background (odd rows)
    text_selected_bg = 47
    drag_drop_target = 48         # Rectangle highlighting a drop target
    nav_highlight = 49            # Gamepad/keyboard: current highlighted item
    nav_windowing_highlight = 50  # Highlight window when using CTRL+TAB
    nav_windowing_dim_bg = 51     # Darken/colorize entire screen behind the CTRL+TAB window list, when active
    modal_window_dim_bg = 52      # Darken/colorize entire screen behind a modal window, when one is active
    count = 53

class ImGuiStyleVar_(Enum):    # imgui.h:1594
    """ Enumeration for PushStyleVar() / PopStyleVar() to temporarily modify the ImGuiStyle structure.
     - The enum only refers to fields of ImGuiStyle which makes sense to be pushed/popped inside UI code.
       During initialization or between frames, feel free to just poke into ImGuiStyle directly.
     - Tip: Use your programming IDE navigation facilities on the names in the _second column_ below to find the actual members and their description.
       In Visual Studio IDE: CTRL+comma ("Edit.GoToAll") can follow symbols in comments, whereas CTRL+F12 ("Edit.GoToImplementation") cannot.
       With Visual Assist installed: ALT+G ("VAssistX.GoToImplementation") can also follow symbols in comments.
     - When changing this enum, you need to update the associated internal table GStyleVarInfo[] accordingly. This is where we link enum values to members offset/type.
    """
    # Enum name --------------------- // Member in ImGuiStyle structure (see ImGuiStyle for descriptions)
    alpha = 0                   # float     Alpha
    disabled_alpha = 1          # float     DisabledAlpha
    window_padding = 2          # ImVec2    WindowPadding
    window_rounding = 3         # float     WindowRounding
    window_border_size = 4      # float     WindowBorderSize
    window_min_size = 5         # ImVec2    WindowMinSize
    window_title_align = 6      # ImVec2    WindowTitleAlign
    child_rounding = 7          # float     ChildRounding
    child_border_size = 8       # float     ChildBorderSize
    popup_rounding = 9          # float     PopupRounding
    popup_border_size = 10      # float     PopupBorderSize
    frame_padding = 11          # ImVec2    FramePadding
    frame_rounding = 12         # float     FrameRounding
    frame_border_size = 13      # float     FrameBorderSize
    item_spacing = 14           # ImVec2    ItemSpacing
    item_inner_spacing = 15     # ImVec2    ItemInnerSpacing
    indent_spacing = 16         # float     IndentSpacing
    cell_padding = 17           # ImVec2    CellPadding
    scrollbar_size = 18         # float     ScrollbarSize
    scrollbar_rounding = 19     # float     ScrollbarRounding
    grab_min_size = 20          # float     GrabMinSize
    grab_rounding = 21          # float     GrabRounding
    tab_rounding = 22           # float     TabRounding
    button_text_align = 23      # ImVec2    ButtonTextAlign
    selectable_text_align = 24  # ImVec2    SelectableTextAlign
    count = 25

class ImGuiButtonFlags_(Enum):    # imgui.h:1626
    """ Flags for InvisibleButton() [extended in imgui_internal.h]"""
    none = 0
    mouse_button_left = 1 << 0    # React on left mouse button (default)
    mouse_button_right = 1 << 1   # React on right mouse button
    mouse_button_middle = 1 << 2  # React on center mouse button

    # [Internal]
    mouse_button_mask_ = Literal[ImGuiButtonFlags_.mouse_button_left] | Literal[ImGuiButtonFlags_.mouse_button_right] | Literal[ImGuiButtonFlags_.mouse_button_middle]
    mouse_button_default_ = Literal[ImGuiButtonFlags_.mouse_button_left]

class ImGuiColorEditFlags_(Enum):    # imgui.h:1639
    """ Flags for ColorEdit3() / ColorEdit4() / ColorPicker3() / ColorPicker4() / ColorButton()"""
    none = 0
    no_alpha = 1 << 1             #              // ColorEdit, ColorPicker, ColorButton: ignore Alpha component (will only read 3 components from the input pointer).
    no_picker = 1 << 2            #              // ColorEdit: disable picker when clicking on color square.
    no_options = 1 << 3           #              // ColorEdit: disable toggling options menu when right-clicking on inputs/small preview.
    no_small_preview = 1 << 4     #              // ColorEdit, ColorPicker: disable color square preview next to the inputs. (e.g. to show only the inputs)
    no_inputs = 1 << 5            #              // ColorEdit, ColorPicker: disable inputs sliders/text widgets (e.g. to show only the small preview color square).
    no_tooltip = 1 << 6           #              // ColorEdit, ColorPicker, ColorButton: disable tooltip when hovering the preview.
    no_label = 1 << 7             #              // ColorEdit, ColorPicker: disable display of inline text label (the label is still forwarded to the tooltip and picker).
    no_side_preview = 1 << 8      #              // ColorPicker: disable bigger color preview on right side of the picker, use small color square preview instead.
    no_drag_drop = 1 << 9         #              // ColorEdit: disable drag and drop target. ColorButton: disable drag and drop source.
    no_border = 1 << 10           #              // ColorButton: disable border (which is enforced by default)

    # User Options (right-click on widget to change some of them).
    alpha_bar = 1 << 16           #              // ColorEdit, ColorPicker: show vertical alpha bar/gradient in picker.
    alpha_preview = 1 << 17       #              // ColorEdit, ColorPicker, ColorButton: display preview as a transparent color over a checkerboard, instead of opaque.
    alpha_preview_half = 1 << 18  #              // ColorEdit, ColorPicker, ColorButton: display half opaque / half checkerboard, instead of opaque.
    hdr = 1 << 19                 #              // (WIP) ColorEdit: Currently only disable 0.0..1.0 limits in RGBA edition (note: you probably want to use ImGuiColorEditFlags_Float flag as well).
    display_rgb = 1 << 20         # [Display]    // ColorEdit: override _display_ type among RGB/HSV/Hex. ColorPicker: select any combination using one or more of RGB/HSV/Hex.
    display_hsv = 1 << 21         # [Display]    // "
    display_hex = 1 << 22         # [Display]    // "
    uint8 = 1 << 23               # [DataType]   // ColorEdit, ColorPicker, ColorButton: _display_ values formatted as 0..255.
    float = 1 << 24               # [DataType]   // ColorEdit, ColorPicker, ColorButton: _display_ values formatted as 0.0..1.0 floats instead of 0..255 integers. No round-trip of value via integers.
    picker_hue_bar = 1 << 25      # [Picker]     // ColorPicker: bar for Hue, rectangle for Sat/Value.
    picker_hue_wheel = 1 << 26    # [Picker]     // ColorPicker: wheel for Hue, triangle for Sat/Value.
    input_rgb = 1 << 27           # [Input]      // ColorEdit, ColorPicker: input and output data in RGB format.
    input_hsv = 1 << 28           # [Input]      // ColorEdit, ColorPicker: input and output data in HSV format.

    # Defaults Options. You can set application defaults using SetColorEditOptions(). The intent is that you probably don't want to
    # override them in most of your calls. Let the user choose via the option menu and/or call SetColorEditOptions() once during startup.
    default_options_ = Literal[ImGuiColorEditFlags_.uint8] | Literal[ImGuiColorEditFlags_.display_rgb] | Literal[ImGuiColorEditFlags_.input_rgb] | Literal[ImGuiColorEditFlags_.picker_hue_bar]

    # [Internal] Masks
    display_mask_ = Literal[ImGuiColorEditFlags_.display_rgb] | Literal[ImGuiColorEditFlags_.display_hsv] | Literal[ImGuiColorEditFlags_.display_hex]
    data_type_mask_ = Literal[ImGuiColorEditFlags_.uint8] | Literal[ImGuiColorEditFlags_.float]
    picker_mask_ = Literal[ImGuiColorEditFlags_.picker_hue_wheel] | Literal[ImGuiColorEditFlags_.picker_hue_bar]
    input_mask_ = Literal[ImGuiColorEditFlags_.input_rgb] | Literal[ImGuiColorEditFlags_.input_hsv]

    # Obsolete names (will be removed)
    # ImGuiColorEditFlags_RGB = ImGuiColorEditFlags_DisplayRGB, ImGuiColorEditFlags_HSV = ImGuiColorEditFlags_DisplayHSV, ImGuiColorEditFlags_HEX = ImGuiColorEditFlags_DisplayHex  // [renamed in 1.69]

class ImGuiSliderFlags_(Enum):    # imgui.h:1684
    """ Flags for DragFloat(), DragInt(), SliderFloat(), SliderInt() etc.
     We use the same sets of flags for DragXXX() and SliderXXX() functions as the features are the same and it makes it easier to swap them.
    """
    none = 0
    always_clamp = 1 << 4        # Clamp value to min/max bounds when input manually with CTRL+Click. By default CTRL+Click allows going out of bounds.
    logarithmic = 1 << 5         # Make the widget logarithmic (linear otherwise). Consider using ImGuiSliderFlags_NoRoundToFormat with this if using a format-string with small amount of digits.
    no_round_to_format = 1 << 6  # Disable rounding underlying value to match precision of the display format string (e.g. %.3 values are rounded to those 3 digits)
    no_input = 1 << 7            # Disable CTRL+Click or Enter key allowing to input text directly into the widget
    invalid_mask_ = 0x7000000F
    # [Internal] We treat using those bits as being potentially a 'float power' argument from the previous API that has got miscast to this enum, and will trigger an assert if needed.

    # Obsolete names (will be removed)

class ImGuiMouseButton_(Enum):    # imgui.h:1701
    """ Identify a mouse button.
     Those values are guaranteed to be stable and we frequently use 0/1 directly. Named enums provided for convenience.
    """
    left = 0
    right = 1
    middle = 2
    count = 5

class ImGuiMouseCursor_(Enum):    # imgui.h:1711
    """ Enumeration for GetMouseCursor()
     User code may request backend to display given cursor by calling SetMouseCursor(), which is why we have some cursors that are marked unused here
    """
    none = -1
    arrow = 0
    text_input = 1   # When hovering over InputText, etc.
    resize_all = 2   # (Unused by Dear ImGui functions)
    resize_ns = 3    # When hovering over an horizontal border
    resize_ew = 4    # When hovering over a vertical border or a column
    resize_nesw = 5  # When hovering over the bottom-left corner of a window
    resize_nwse = 6  # When hovering over the bottom-right corner of a window
    hand = 7         # (Unused by Dear ImGui functions. Use for e.g. hyperlinks)
    not_allowed = 8  # When hovering something with disallowed interaction. Usually a crossed circle.
    count = 9

class ImGuiCond_(Enum):    # imgui.h:1729
    """ Enumeration for ImGui::SetWindow***(), SetNextWindow***(), SetNextItem***() functions
     Represent a condition.
     Important: Treat as a regular enum! Do NOT combine multiple values using binary operators! All the functions above treat 0 as a shortcut to ImGuiCond_Always.
    """
    none = 0                 # No condition (always set the variable), same as _Always
    always = 1 << 0          # No condition (always set the variable)
    once = 1 << 1            # Set the variable once per runtime session (only the first call will succeed)
    first_use_ever = 1 << 2  # Set the variable if the object/window has no persistently saved data (no entry in .ini file)
    appearing = 1 << 3       # Set the variable if the object/window is appearing after being hidden/inactive (or the first time)

#-----------------------------------------------------------------------------
# [SECTION] Helpers: Memory allocations macros, ImVector<>
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# IM_MALLOC(), IM_FREE(), IM_NEW(), IM_PLACEMENT_NEW(), IM_DELETE()
# We call C++ constructor on own allocated memory via the placement "new(ptr) Type()" syntax.
# Defining a custom placement new() with a custom parameter allows us to bypass including <new> which on some platforms complains when user has disabled exceptions.
#-----------------------------------------------------------------------------

class ImNewWrapper:    # imgui.h:1748
    pass
# This is only required so we can use the symmetrical new()

#-----------------------------------------------------------------------------
# ImVector<>
# Lightweight std::vector<>-like class to avoid dragging dependencies (also, some implementations of STL with debug enabled are absurdly slow, we bypass it so our code runs fast in debug).
#-----------------------------------------------------------------------------
# - You generally do NOT need to care or use this ever. But we need to make it available in imgui.h because some of our public structures are relying on it.
# - We use std-like naming convention here, which is a little unusual for this codebase.
# - Important: clear() frees memory, resize(0) keep the allocated buffer. We use resize(0) a lot to intentionally recycle allocated buffers across frames and amortize our costs.
# - Important: our implementation does NOT call C++ constructors/destructors, we treat everything as raw data! This is intentional but be extra mindful of that,
#   Do NOT use this class as a std::vector replacement in your own code! Many of the structures used by dear imgui can be safely initialized by a zero-memset.
#-----------------------------------------------------------------------------


#-----------------------------------------------------------------------------
# [SECTION] ImGuiStyle
#-----------------------------------------------------------------------------
# You may modify the ImGui::GetStyle() main instance during initialization and before NewFrame().
# During the frame, use ImGui::PushStyleVar(ImGuiStyleVar_XXXX)/PopStyleVar() to alter the main style values,
# and ImGui::PushStyleColor(ImGuiCol_XXX)/PopStyleColor() for colors.
#-----------------------------------------------------------------------------

class ImGuiStyle:    # imgui.h:1840
    alpha:float                                                # Global alpha applies to everything in Dear ImGui.    # imgui.h:1842
    disabled_alpha:float                                       # Additional alpha multiplier applied by BeginDisabled(). Multiply over current value of Alpha.    # imgui.h:1843
    window_padding:ImVec2                                      # Padding within a window.    # imgui.h:1844
    window_rounding:float                                      # Radius of window corners rounding. Set to 0.0 to have rectangular windows. Large values tend to lead to variety of artifacts and are not recommended.    # imgui.h:1845
    window_border_size:float                                   # Thickness of border around windows. Generally set to 0.0 or 1.0. (Other values are not well tested and more CPU/GPU costly).    # imgui.h:1846
    window_min_size:ImVec2                                     # Minimum window size. This is a global setting. If you want to constraint individual windows, use SetNextWindowSizeConstraints().    # imgui.h:1847
    window_title_align:ImVec2                                  # Alignment for title bar text. Defaults to (0.0,0.5) for left-aligned,vertically centered.    # imgui.h:1848
    window_menu_button_position:ImGuiDir                       # Side of the collapsing/docking button in the title bar (None/Left/Right). Defaults to ImGuiDir_Left.    # imgui.h:1849
    child_rounding:float                                       # Radius of child window corners rounding. Set to 0.0 to have rectangular windows.    # imgui.h:1850
    child_border_size:float                                    # Thickness of border around child windows. Generally set to 0.0 or 1.0. (Other values are not well tested and more CPU/GPU costly).    # imgui.h:1851
    popup_rounding:float                                       # Radius of popup window corners rounding. (Note that tooltip windows use WindowRounding)    # imgui.h:1852
    popup_border_size:float                                    # Thickness of border around popup/tooltip windows. Generally set to 0.0 or 1.0. (Other values are not well tested and more CPU/GPU costly).    # imgui.h:1853
    frame_padding:ImVec2                                       # Padding within a framed rectangle (used by most widgets).    # imgui.h:1854
    frame_rounding:float                                       # Radius of frame corners rounding. Set to 0.0 to have rectangular frame (used by most widgets).    # imgui.h:1855
    frame_border_size:float                                    # Thickness of border around frames. Generally set to 0.0 or 1.0. (Other values are not well tested and more CPU/GPU costly).    # imgui.h:1856
    item_spacing:ImVec2                                        # Horizontal and vertical spacing between widgets/lines.    # imgui.h:1857
    item_inner_spacing:ImVec2                                  # Horizontal and vertical spacing between within elements of a composed widget (e.g. a slider and its label).    # imgui.h:1858
    cell_padding:ImVec2                                        # Padding within a table cell    # imgui.h:1859
    touch_extra_padding:ImVec2                                 # Expand reactive bounding box for touch-based system where touch position is not accurate enough. Unfortunately we don't sort widgets so priority on overlap will always be given to the first widget. So don't grow this too much!    # imgui.h:1860
    indent_spacing:float                                       # Horizontal indentation when e.g. entering a tree node. Generally == (FontSize + FramePadding.x*2).    # imgui.h:1861
    columns_min_spacing:float                                  # Minimum horizontal spacing between two columns. Preferably > (FramePadding.x + 1).    # imgui.h:1862
    scrollbar_size:float                                       # Width of the vertical scrollbar, Height of the horizontal scrollbar.    # imgui.h:1863
    scrollbar_rounding:float                                   # Radius of grab corners for scrollbar.    # imgui.h:1864
    grab_min_size:float                                        # Minimum width/height of a grab box for slider/scrollbar.    # imgui.h:1865
    grab_rounding:float                                        # Radius of grabs corners rounding. Set to 0.0 to have rectangular slider grabs.    # imgui.h:1866
    log_slider_deadzone:float                                  # The size in pixels of the dead-zone around zero on logarithmic sliders that cross zero.    # imgui.h:1867
    tab_rounding:float                                         # Radius of upper corners of a tab. Set to 0.0 to have rectangular tabs.    # imgui.h:1868
    tab_border_size:float                                      # Thickness of border around tabs.    # imgui.h:1869
    tab_min_width_for_close_button:float                       # Minimum width for close button to appears on an unselected tab when hovered. Set to 0.0 to always show when hovering, set to FLT_MAX to never show close button unless selected.    # imgui.h:1870
    color_button_position:ImGuiDir                             # Side of the color button in the ColorEdit4 widget (left/right). Defaults to ImGuiDir_Right.    # imgui.h:1871
    button_text_align:ImVec2                                   # Alignment of button text when button is larger than text. Defaults to (0.5, 0.5) (centered).    # imgui.h:1872
    selectable_text_align:ImVec2                               # Alignment of selectable text. Defaults to (0.0, 0.0) (top-left aligned). It's generally important to keep this left-aligned if you want to lay multiple items on a same line.    # imgui.h:1873
    display_window_padding:ImVec2                              # Window position are clamped to be visible within the display area or monitors by at least this amount. Only applies to regular windows.    # imgui.h:1874
    display_safe_area_padding:ImVec2                           # If you cannot see the edges of your screen (e.g. on a TV) increase the safe area padding. Apply to popups/tooltips as well regular windows. NB: Prefer configuring your TV sets correctly!    # imgui.h:1875
    mouse_cursor_scale:float                                   # Scale software rendered mouse cursor (when io.MouseDrawCursor is enabled). May be removed later.    # imgui.h:1876
    anti_aliased_lines:bool                                    # Enable anti-aliased lines/borders. Disable if you are really tight on CPU/GPU. Latched at the beginning of the frame (copied to ImDrawList).    # imgui.h:1877
    anti_aliased_lines_use_tex:bool                            # Enable anti-aliased lines/borders using textures where possible. Require backend to render with bilinear filtering (NOT point/nearest filtering). Latched at the beginning of the frame (copied to ImDrawList).    # imgui.h:1878
    anti_aliased_fill:bool                                     # Enable anti-aliased edges around filled shapes (rounded rectangles, circles, etc.). Disable if you are really tight on CPU/GPU. Latched at the beginning of the frame (copied to ImDrawList).    # imgui.h:1879
    curve_tessellation_tol:float                               # Tessellation tolerance when using PathBezierCurveTo() without a specific number of segments. Decrease for highly tessellated curves (higher quality, more polygons), increase to reduce quality.    # imgui.h:1880
    circle_tessellation_max_error:float                        # Maximum error (in pixels) allowed when using AddCircle()/AddCircleFilled() or drawing rounded corner rectangles with no explicit segment count specified. Decrease for higher quality but more geometry.    # imgui.h:1881

    def __init__(self) -> None:                                # imgui.h:1884
        pass
    def scale_all_sizes(self, scale_factor: float) -> None:    # imgui.h:1885
        pass

#-----------------------------------------------------------------------------
# [SECTION] ImGuiIO
#-----------------------------------------------------------------------------
# Communicate most settings and inputs/outputs to Dear ImGui using this structure.
# Access via ImGui::GetIO(). Read 'Programmer guide' section in .cpp file for general usage.
#-----------------------------------------------------------------------------

class ImGuiKeyData:    # imgui.h:1897
    """ [Internal] Storage used by IsKeyDown(), IsKeyPressed() etc functions.
     If prior to 1.87 you used io.KeysDownDuration[] (which was marked as internal), you should use GetKeyData(key)->DownDuration and not io.KeysData[key]->DownDuration.
    """
    down:bool                 # True for if key is down    # imgui.h:1899
    down_duration:float       # Duration the key has been down (<0.0: not pressed, 0.0: just pressed, >0.0: time held)    # imgui.h:1900
    down_duration_prev:float  # Last frame duration the key has been down    # imgui.h:1901
    analog_value:float        # 0.0..1.0 for gamepad values    # imgui.h:1902

class ImGuiIO:    # imgui.h:1905
    #------------------------------------------------------------------
    # Configuration                            // Default value
    #------------------------------------------------------------------

    config_flags:ImGuiConfigFlags                                                   # = 0              // See ImGuiConfigFlags_ enum. Set by user/application. Gamepad/keyboard navigation options, etc.    # imgui.h:1911
    backend_flags:ImGuiBackendFlags                                                 # = 0              // See ImGuiBackendFlags_ enum. Set by backend (imgui_impl_xxx files or custom backend) to communicate features supported by the backend.    # imgui.h:1912
    display_size:ImVec2                                                             # <unset>          // Main display size, in pixels (generally == GetMainViewport()->Size). May change every frame.    # imgui.h:1913
    delta_time:float                                                                # = 1.0/60.0     // Time elapsed since last frame, in seconds. May change every frame.    # imgui.h:1914
    ini_saving_rate:float                                                           # = 5.0           // Minimum time between saving positions/sizes to .ini file, in seconds.    # imgui.h:1915
    ini_filename:str                                                                # = "imgui.ini"    // Path to .ini file (important: default "imgui.ini" is relative to current working dir!). Set None to disable automatic .ini loading/saving or if you want to manually call LoadIniSettingsXXX() / SaveIniSettingsXXX() functions.    # imgui.h:1916
    log_filename:str                                                                # = "imgui_log.txt"// Path to .log file (default parameter to ImGui::LogToFile when no file is specified).    # imgui.h:1917
    mouse_double_click_time:float                                                   # = 0.30          // Time for a double-click, in seconds.    # imgui.h:1918
    mouse_double_click_max_dist:float                                               # = 6.0           // Distance threshold to stay in to validate a double-click, in pixels.    # imgui.h:1919
    mouse_drag_threshold:float                                                      # = 6.0           // Distance threshold before considering we are dragging.    # imgui.h:1920
    key_repeat_delay:float                                                          # = 0.250         // When holding a key/button, time before it starts repeating, in seconds (for buttons in Repeat mode, etc.).    # imgui.h:1921
    key_repeat_rate:float                                                           # = 0.050         // When holding a key/button, rate at which it repeats, in seconds.    # imgui.h:1922
    user_data:None                                                                  # = None           // Store your own data for retrieval by callbacks.    # imgui.h:1923

    fonts:ImFontAtlas                                                               # <auto>           // Font atlas: load, rasterize and pack one or more fonts into a single texture.    # imgui.h:1925
    font_global_scale:float                                                         # = 1.0           // Global scale all fonts    # imgui.h:1926
    font_allow_user_scaling:bool                                                    # = False          // Allow user scaling text of individual window with CTRL+Wheel.    # imgui.h:1927
    font_default:ImFont                                                             # = None           // Font to use on NewFrame(). Use None to uses Fonts->Fonts[0].    # imgui.h:1928
    display_framebuffer_scale:ImVec2                                                # = (1, 1)         // For retina display or other situations where window coordinates are different from framebuffer coordinates. This generally ends up in ImDrawData::FramebufferScale.    # imgui.h:1929

    # Miscellaneous options
    mouse_draw_cursor:bool                                                          # = False          // Request ImGui to draw a mouse cursor for you (if you are on a platform without a mouse cursor). Cannot be easily renamed to 'io.ConfigXXX' because this is frequently used by backend implementations.    # imgui.h:1932
    config_mac_osx_behaviors:bool                                                   # = defined(__APPLE__) // OS X style: Text editing cursor movement using Alt instead of Ctrl, Shortcuts using Cmd/Super instead of Ctrl, Line/Text Start and End using Cmd+Arrows instead of Home/End, Double click selects by word instead of selecting whole text, Multi-selection in lists uses Cmd/Super instead of Ctrl.    # imgui.h:1933
    config_input_trickle_event_queue:bool                                           # = True           // Enable input queue trickling: some types of events submitted during the same frame (e.g. button down + up) will be spread over multiple frames, improving interactions with low framerates.    # imgui.h:1934
    config_input_text_cursor_blink:bool                                             # = True           // Enable blinking cursor (optional as some users consider it to be distracting).    # imgui.h:1935
    config_drag_click_to_input_text:bool                                            # = False          // [BETA] Enable turning DragXXX widgets into text input with a simple mouse click-release (without moving). Not desirable on devices without a keyboard.    # imgui.h:1936
    config_windows_resize_from_edges:bool                                           # = True           // Enable resizing of windows from their edges and from the lower-left corner. This requires (io.BackendFlags & ImGuiBackendFlags_HasMouseCursors) because it needs mouse cursor feedback. (This used to be a per-window ImGuiWindowFlags_ResizeFromAnySide flag)    # imgui.h:1937
    config_windows_move_from_title_bar_only:bool                                    # = False       // Enable allowing to move windows only when clicking on their title bar. Does not apply to windows without a title bar.    # imgui.h:1938
    config_memory_compact_timer:float                                               # = 60.0          // Timer (in seconds) to free transient windows/tables memory buffers when unused. Set to -1.0 to disable.    # imgui.h:1939

    #------------------------------------------------------------------
    # Platform Functions
    # (the imgui_impl_xxxx backend files are setting those up for you)
    #------------------------------------------------------------------

    # Optional: Platform/Renderer backend name (informational only! will be displayed in About Window) + User data for backend/wrappers to store their own stuff.
    backend_platform_name:str                                                       # = None    # imgui.h:1947
    backend_renderer_name:str                                                       # = None    # imgui.h:1948
    backend_platform_user_data:None                                                 # = None           // User data for platform backend    # imgui.h:1949
    backend_renderer_user_data:None                                                 # = None           // User data for renderer backend    # imgui.h:1950
    backend_language_user_data:None                                                 # = None           // User data for non C++ programming language backend    # imgui.h:1951

    # Optional: Access OS clipboard
    # (default to use native Win32 clipboard on Windows, otherwise uses a private clipboard. Override to access OS clipboard on other architectures)
    clipboard_user_data:None                                                        # imgui.h:1957


    #------------------------------------------------------------------
    # Input - Call before calling NewFrame()
    #------------------------------------------------------------------

    # Input Functions
    def add_key_event(self, key: ImGuiKey, down: bool) -> None:                     # imgui.h:1973
        """ Queue a new key down/up event. Key should be "translated" (as in, generally ImGuiKey_A matches the key end-user would use to emit an 'A' character)"""
        pass
    def add_key_analog_event(self, key: ImGuiKey, down: bool, v: float) -> None:    # imgui.h:1974
        """ Queue a new key down/up event for analog values (e.g. ImGuiKey_Gamepad_ values). Dead-zones should be handled by the backend."""
        pass
    def add_mouse_pos_event(self, x: float, y: float) -> None:                      # imgui.h:1975
        """ Queue a mouse position update. Use -FLT_MAX,-FLT_MAX to signify no mouse (e.g. app not focused and not hovered)"""
        pass
    def add_mouse_button_event(self, button: int, down: bool) -> None:              # imgui.h:1976
        """ Queue a mouse button change"""
        pass
    def add_mouse_wheel_event(self, wh_x: float, wh_y: float) -> None:              # imgui.h:1977
        """ Queue a mouse wheel update"""
        pass
    def add_focus_event(self, focused: bool) -> None:                               # imgui.h:1978
        """ Queue a gain/loss of focus for the application (generally based on OS/platform focus of your window)"""
        pass
    def add_input_character(self, c: int) -> None:                                  # imgui.h:1979
        """ Queue a new character input"""
        pass
    def add_input_character_utf16(self, c: ImWchar16) -> None:                      # imgui.h:1980
        """ Queue a new character input from an UTF-16 character, it can be a surrogate"""
        pass
    def add_input_characters_utf8(self, str: str) -> None:                          # imgui.h:1981
        """ Queue a new characters input from an UTF-8 string"""
        pass

    def set_key_event_native_data(                                                  # imgui.h:1983
        self,
        key: ImGuiKey,
        native_keycode: int,
        native_scancode: int,
        native_legacy_index: int = -1
        ) -> None:
        """ [Optional] Specify index for legacy <1.87 IsKeyXXX() functions with native indices + specify native keycode, scancode."""
        pass
    def set_app_accepting_events(self, accepting_events: bool) -> None:             # imgui.h:1984
        """ Set master flag for accepting key/mouse/text events (default to True). Useful if you have native dialog boxes that are interrupting your application loop/refresh, and you want to disable events being queued while your app is frozen."""
        pass
    def clear_input_characters(self) -> None:                                       # imgui.h:1985
        """ [Internal] Clear the text input buffer manually"""
        pass
    def clear_input_keys(self) -> None:                                             # imgui.h:1986
        """ [Internal] Release all keys"""
        pass

    #------------------------------------------------------------------
    # Output - Updated by NewFrame() or EndFrame()/Render()
    # (when reading from the io.WantCaptureMouse, io.WantCaptureKeyboard flags to dispatch your inputs, it is
    #  generally easier and more correct to use their state BEFORE calling NewFrame(). See FAQ for details!)
    #------------------------------------------------------------------

    want_capture_mouse:bool                                                         # Set when Dear ImGui will use mouse inputs, in this case do not dispatch them to your main game/application (either way, always pass on mouse inputs to imgui). (e.g. unclicked mouse is hovering over an imgui window, widget is active, mouse was clicked over an imgui window, etc.).    # imgui.h:1994
    want_capture_keyboard:bool                                                      # Set when Dear ImGui will use keyboard inputs, in this case do not dispatch them to your main game/application (either way, always pass keyboard inputs to imgui). (e.g. InputText active, or an imgui window is focused and navigation is enabled, etc.).    # imgui.h:1995
    want_text_input:bool                                                            # Mobile/console: when set, you may display an on-screen keyboard. This is set by Dear ImGui when it wants textual keyboard input to happen (e.g. when a InputText widget is active).    # imgui.h:1996
    want_set_mouse_pos:bool                                                         # MousePos has been altered, backend should reposition mouse on next frame. Rarely used! Set only when ImGuiConfigFlags_NavEnableSetMousePos flag is enabled.    # imgui.h:1997
    want_save_ini_settings:bool                                                     # When manual .ini load/save is active (io.IniFilename == None), this will be set to notify your application that you can call SaveIniSettingsToMemory() and save yourself. Important: clear io.WantSaveIniSettings yourself after saving!    # imgui.h:1998
    nav_active:bool                                                                 # Keyboard/Gamepad navigation is currently allowed (will handle ImGuiKey_NavXXX events) = a window is focused and it doesn't use the ImGuiWindowFlags_NoNavInputs flag.    # imgui.h:1999
    nav_visible:bool                                                                # Keyboard/Gamepad navigation is visible and allowed (will handle ImGuiKey_NavXXX events).    # imgui.h:2000
    framerate:float                                                                 # Rough estimate of application framerate, in frame per second. Solely for convenience. Rolling average estimation based on io.DeltaTime over 120 frames.    # imgui.h:2001
    metrics_render_vertices:int                                                     # Vertices output during last call to Render()    # imgui.h:2002
    metrics_render_indices:int                                                      # Indices output during last call to Render() = number of triangles * 3    # imgui.h:2003
    metrics_render_windows:int                                                      # Number of visible windows    # imgui.h:2004
    metrics_active_windows:int                                                      # Number of active windows    # imgui.h:2005
    metrics_active_allocations:int                                                  # Number of active allocations, updated by MemAlloc/MemFree based on current context. May be off if you have multiple imgui contexts.    # imgui.h:2006
    mouse_delta:ImVec2                                                              # imgui.h:2007
    # Mouse delta. Note that this is zero if either current or previous position are invalid (-FLT_MAX,-FLT_MAX), so a disappearing/reappearing mouse won't have a huge delta.

    # Legacy: before 1.87, we required backend to fill io.KeyMap[] (imgui->native map) during initialization and io.KeysDown[] (native indices) every frame.
    # This is still temporarily supported as a legacy feature. However the new preferred scheme is for backend to call io.AddKeyEvent().

    #------------------------------------------------------------------
    # [Internal] Dear ImGui will maintain those fields. Forward compatibility not guaranteed!
    #------------------------------------------------------------------

    # Main Input State
    # (this block used to be written by backend, since 1.87 it is best to NOT write to those directly, call the AddXXX functions above instead)
    # (reading from those variables is fair game, as they are extremely unlikely to be moving anywhere)
    mouse_pos:ImVec2                                                                # Mouse position, in pixels. Set to ImVec2(-FLT_MAX, -FLT_MAX) if mouse is unavailable (on another screen, etc.)    # imgui.h:2023
    mouse_down:np.ndarray                                                           # ndarray[type=bool, size=5]  # Mouse buttons: 0=left, 1=right, 2=middle + extras (ImGuiMouseButton_COUNT == 5). Dear ImGui mostly uses left and right buttons. Others buttons allows us to track if the mouse is being used by your application + available to user as a convenience via IsMouse** API.    # imgui.h:2024
    mouse_wheel:float                                                               # Mouse wheel Vertical: 1 unit scrolls about 5 lines text.    # imgui.h:2025
    mouse_wheel_h:float                                                             # Mouse wheel Horizontal. Most users don't have a mouse with an horizontal wheel, may not be filled by all backends.    # imgui.h:2026
    key_ctrl:bool                                                                   # Keyboard modifier down: Control    # imgui.h:2027
    key_shift:bool                                                                  # Keyboard modifier down: Shift    # imgui.h:2028
    key_alt:bool                                                                    # Keyboard modifier down: Alt    # imgui.h:2029
    key_super:bool                                                                  # Keyboard modifier down: Cmd/Super/Windows    # imgui.h:2030

    # Other state maintained from data above + IO function calls
    key_mods:ImGuiModFlags                                                          # Key mods flags (same as io.KeyCtrl/KeyShift/KeyAlt/KeySuper but merged into flags), updated by NewFrame()    # imgui.h:2034
    want_capture_mouse_unless_popup_close:bool                                      # Alternative to WantCaptureMouse: (WantCaptureMouse == True && WantCaptureMouseUnlessPopupClose == False) when a click over None is expected to close a popup.    # imgui.h:2036
    mouse_pos_prev:ImVec2                                                           # Previous mouse position (note that MouseDelta is not necessary == MousePos-MousePosPrev, in case either position is invalid)    # imgui.h:2037
    mouse_clicked_time:np.ndarray                                                   # ndarray[type=double, size=5]  # Time of last click (used to figure out double-click)    # imgui.h:2039
    mouse_clicked:np.ndarray                                                        # ndarray[type=bool, size=5]  # Mouse button went from !Down to Down (same as MouseClickedCount[x] != 0)    # imgui.h:2040
    mouse_double_clicked:np.ndarray                                                 # ndarray[type=bool, size=5]  # Has mouse button been double-clicked? (same as MouseClickedCount[x] == 2)    # imgui.h:2041
    mouse_clicked_count:np.ndarray                                                  # ndarray[type=ImU16, size=5]  # == 0 (not clicked), == 1 (same as MouseClicked[]), == 2 (double-clicked), == 3 (triple-clicked) etc. when going from !Down to Down    # imgui.h:2042
    mouse_clicked_last_count:np.ndarray                                             # ndarray[type=ImU16, size=5]  # Count successive number of clicks. Stays valid after mouse release. Reset after another click is done.    # imgui.h:2043
    mouse_released:np.ndarray                                                       # ndarray[type=bool, size=5]  # Mouse button went from Down to !Down    # imgui.h:2044
    mouse_down_owned:np.ndarray                                                     # ndarray[type=bool, size=5]  # Track if button was clicked inside a dear imgui window or over None blocked by a popup. We don't request mouse capture from the application if click started outside ImGui bounds.    # imgui.h:2045
    mouse_down_owned_unless_popup_close:np.ndarray                                  # ndarray[type=bool, size=5]  # Track if button was clicked inside a dear imgui window.    # imgui.h:2046
    mouse_down_duration:np.ndarray                                                  # ndarray[type=float, size=5]  # Duration the mouse button has been down (0.0 == just clicked)    # imgui.h:2047
    mouse_down_duration_prev:np.ndarray                                             # ndarray[type=float, size=5]  # Previous time the mouse button has been down    # imgui.h:2048
    mouse_drag_max_distance_sqr:np.ndarray                                          # ndarray[type=float, size=5]  # Squared maximum distance of how much mouse has traveled from the clicking point (used for moving thresholds)    # imgui.h:2049
    pen_pressure:float                                                              # Touch/Pen pressure (0.0 to 1.0, should be >0.0 only when MouseDown[0] == True). Helper storage currently unused by Dear ImGui.    # imgui.h:2052
    app_focus_lost:bool                                                             # Only modify via AddFocusEvent()    # imgui.h:2053
    app_accepting_events:bool                                                       # Only modify via SetAppAcceptingEvents()    # imgui.h:2054
    backend_using_legacy_key_arrays:ImS8                                            # -1: unknown, 0: using AddKeyEvent(), 1: using legacy io.KeysDown[]    # imgui.h:2055
    backend_using_legacy_nav_input_array:bool                                       # 0: using AddKeyAnalogEvent(), 1: writing to legacy io.NavInputs[] directly    # imgui.h:2056
    input_queue_surrogate:ImWchar16                                                 # For AddInputCharacterUTF16()    # imgui.h:2057
    input_queue_characters:List[ImWchar]                                            # Queue of _characters_ input (obtained by platform backend). Fill using AddInputCharacter() helper.    # imgui.h:2058

    def __init__(self) -> None:                                                     # imgui.h:2060
        pass

#-----------------------------------------------------------------------------
# [SECTION] Misc data structures
#-----------------------------------------------------------------------------

class ImGuiInputTextCallbackData:    # imgui.h:2076
    """ Shared state of InputText(), passed as an argument to your callback when a ImGuiInputTextFlags_Callback* flag is used.
     The callback function should return 0 by default.
     Callbacks (follow a flag name and see comments in ImGuiInputTextFlags_ declarations for more details)
     - ImGuiInputTextFlags_CallbackEdit:        Callback on buffer edit (note that InputText() already returns True on edit, the callback is useful mainly to manipulate the underlying buffer while focus is active)
     - ImGuiInputTextFlags_CallbackAlways:      Callback on each iteration
     - ImGuiInputTextFlags_CallbackCompletion:  Callback on pressing TAB
     - ImGuiInputTextFlags_CallbackHistory:     Callback on pressing Up/Down arrows
     - ImGuiInputTextFlags_CallbackCharFilter:  Callback on character inputs to replace or discard them. Modify 'EventChar' to replace or discard, or return 1 in callback to discard.
     - ImGuiInputTextFlags_CallbackResize:      Callback on buffer capacity changes request (beyond 'buf_size' parameter value), allowing the string to grow.
    """
    event_flag:ImGuiInputTextFlags                                                # One ImGuiInputTextFlags_Callback*    // Read-only    # imgui.h:2078
    flags:ImGuiInputTextFlags                                                     # What user passed to InputText()      // Read-only    # imgui.h:2079
    user_data:None                                                                # What user passed to InputText()      // Read-only    # imgui.h:2080

    # Arguments for the different callback events
    # - To modify the text buffer in a callback, prefer using the InsertChars() / DeleteChars() function. InsertChars() will take care of calling the resize callback if necessary.
    # - If you know your edits are not going to resize the underlying buffer allocation, you may modify the contents of 'Buf[]' directly. You need to update 'BufTextLen' accordingly (0 <= BufTextLen < BufSize) and set 'BufDirty'' to True so InputText can update its internal state.
    event_char:ImWchar                                                            # Character input                      // Read-write   // [CharFilter] Replace character with another one, or set to zero to drop. return 1 is equivalent to setting EventChar=0;    # imgui.h:2085
    event_key:ImGuiKey                                                            # Key pressed (Up/Down/TAB)            // Read-only    // [Completion,History]    # imgui.h:2086
    buf:char                                                                      # Text buffer                          // Read-write   // [Resize] Can replace pointer / [Completion,History,Always] Only write to pointed data, don't replace the actual pointer!    # imgui.h:2087
    buf_text_len:int                                                              # Text length (in bytes)               // Read-write   // [Resize,Completion,History,Always] Exclude zero-terminator storage. In C land: == strlen(some_text), in C++ land: string.length()    # imgui.h:2088
    buf_size:int                                                                  # Buffer size (in bytes) = capacity+1  // Read-only    // [Resize,Completion,History,Always] Include zero-terminator storage. In C land == ARRAYSIZE(my_char_array), in C++ land: string.capacity()+1    # imgui.h:2089
    buf_dirty:bool                                                                # Set if you modify Buf/BufTextLen!    // Write        // [Completion,History,Always]    # imgui.h:2090
    cursor_pos:int                                                                #                                      // Read-write   // [Completion,History,Always]    # imgui.h:2091
    selection_start:int                                                           #                                      // Read-write   // [Completion,History,Always] == to SelectionEnd when no selection)    # imgui.h:2092
    selection_end:int                                                             #                                      // Read-write   // [Completion,History,Always]    # imgui.h:2093

    # Helper functions for text manipulation.
    # Use those function to benefit from the CallbackResize behaviors. Calling those function reset the selection.
    def __init__(self) -> None:                                                   # imgui.h:2097
        pass
    def delete_chars(self, pos: int, bytes_count: int) -> None:                   # imgui.h:2098
        pass
    def insert_chars(self, pos: int, text: str, text_end: str = None) -> None:    # imgui.h:2099
        pass

class ImGuiSizeCallbackData:    # imgui.h:2107
    """ Resizing callback data to apply custom constraint. As enabled by SetNextWindowSizeConstraints(). Callback is called during the next Begin().
     NB: For basic min/max size constraint on each axis you don't need to use the callback! The SetNextWindowSizeConstraints() parameters are enough.
    """
    user_data:None       # Read-only.   What user passed to SetNextWindowSizeConstraints()    # imgui.h:2109
    pos:ImVec2           # Read-only.   Window position, for reference.    # imgui.h:2110
    current_size:ImVec2  # Read-only.   Current window size.    # imgui.h:2111
    desired_size:ImVec2  # Read-write.  Desired size, based on user's mouse position. Write to this field to restrain resizing.    # imgui.h:2112

class ImGuiPayload:    # imgui.h:2116
    """ Data payload for Drag and Drop operations: AcceptDragDropPayload(), GetDragDropPayload()"""
    # Members
    data:None                      # Data (copied and owned by dear imgui)    # imgui.h:2119
    data_size:int                  # Data size    # imgui.h:2120

    # [Internal]
    source_id:ImGuiID              # Source item id    # imgui.h:2123
    source_parent_id:ImGuiID       # Source parent id (if available)    # imgui.h:2124
    data_frame_count:int           # Data timestamp    # imgui.h:2125
    preview:bool                   # Set when AcceptDragDropPayload() was called and mouse has been hovering the target item (nb: handle overlapping drag targets)    # imgui.h:2127
    delivery:bool                  # Set when AcceptDragDropPayload() was called and mouse button is released over the target item.    # imgui.h:2128

    def __init__(self) -> None:    # imgui.h:2130
        pass

class ImGuiTableColumnSortSpecs:    # imgui.h:2138
    """ Sorting specification for one column of a table (sizeof == 12 bytes)"""
    column_user_id:ImGuiID         # User id of the column (if specified by a TableSetupColumn() call)    # imgui.h:2140
    column_index:ImS16             # Index of the column    # imgui.h:2141
    sort_order:ImS16               # Index within parent ImGuiTableSortSpecs (always stored in order starting from 0, tables sorted on a single criteria will always have a 0 here)    # imgui.h:2142

    def __init__(self) -> None:    # imgui.h:2145
        pass

class ImGuiTableSortSpecs:    # imgui.h:2152
    """ Sorting specifications for a table (often handling sort specs for a single column, occasionally more)
     Obtained by calling TableGetSortSpecs().
     When 'SpecsDirty == True' you can sort your data. It will be True with sorting specs have changed since last call, or the first time.
     Make sure to set 'SpecsDirty = False' after sorting, else you may wastefully sort your data every frame!
    """
    specs:ImGuiTableColumnSortSpecs  # Pointer to sort spec array.    # imgui.h:2154
    specs_count:int                  # Sort spec count. Most often 1. May be > 1 when ImGuiTableFlags_SortMulti is enabled. May be == 0 when ImGuiTableFlags_SortTristate is enabled.    # imgui.h:2155
    specs_dirty:bool                 # Set to True when specs have changed since last time! Use this to sort again, then clear the flag.    # imgui.h:2156

    def __init__(self) -> None:      # imgui.h:2158
        pass

#-----------------------------------------------------------------------------
# [SECTION] Helpers (ImGuiOnceUponAFrame, ImGuiTextFilter, ImGuiTextBuffer, ImGuiStorage, ImGuiListClipper, ImColor)
#-----------------------------------------------------------------------------

# Helper: Unicode defines

class ImGuiOnceUponAFrame:    # imgui.h:2175
    """ Helper: Execute a block of code at maximum once a frame. Convenient if you want to quickly create an UI within deep-nested code that runs multiple times every frame.
     Usage: static ImGuiOnceUponAFrame oaf; if (oaf) ImGui::Text("This will be called only once per frame");
    """
    def __init__(self) -> None:    # imgui.h:2177
        pass
    ref_frame:int                  # imgui.h:2178

class ImGuiTextFilter:    # imgui.h:2183
    """ Helper: Parse and apply text filters. In format "aaaaa[,bbbb][,ccccc]" """
    def __init__(self, default_filter: str = "") -> None:                            # imgui.h:2185
        pass
    def draw(self, label: str = "Filter (inc,-exc)", width: float = 0.0) -> bool:    # imgui.h:2186
        """ Helper calling InputText+Build"""
        pass
    def pass_filter(self, text: str, text_end: str = None) -> bool:                  # imgui.h:2187
        pass
    def build(self) -> None:                                                         # imgui.h:2188
        pass

    filters:List[ImGuiTextRange]                                                     # imgui.h:2204
    count_grep:int                                                                   # imgui.h:2205

class ImGuiTextBuffer:    # imgui.h:2210
    """ Helper: Growable text buffer for logging/accumulating text
     (this could be called 'ImGuiTextBuilder' / 'ImGuiStringBuilder')
    """
    buf:List[char]                                              # imgui.h:2212

    def __init__(self) -> None:                                 # imgui.h:2215
        pass
    def append(self, str: str, str_end: str = None) -> None:    # imgui.h:2224
        pass
    def appendf(self, fmt: str) -> None:                        # imgui.h:2225
        pass

class ImGuiStorage:    # imgui.h:2237
    """ Helper: Key->Value storage
     Typically you don't have to worry about this since a storage is held within each Window.
     We use it to e.g. store collapse state for a tree (Int 0/1)
     This is optimized for efficient lookup (dichotomy into a contiguous buffer) and rare insertion (typically tied to user interactions aka max once a frame)
     You can use it as custom user storage for temporary values. Declare your own storage if, for example:
     - You want to manipulate the open/close state of a particular sub-tree in your interface (tree node uses Int 0/1 to store their state).
     - You want to store custom debug data easily without adding or editing structures in your code (probably not efficient, but convenient)
     Types are NOT stored, so it is up to you to make sure your Key don't collide with different types.
    """

    data:List[ImGuiStoragePair]                                                    # imgui.h:2249

    def get_int(self, key: ImGuiID, default_val: int = 0) -> int:                  # imgui.h:2255
        pass
    def set_int(self, key: ImGuiID, val: int) -> None:                             # imgui.h:2256
        pass
    def get_bool(self, key: ImGuiID, default_val: bool = False) -> bool:           # imgui.h:2257
        pass
    def set_bool(self, key: ImGuiID, val: bool) -> None:                           # imgui.h:2258
        pass
    def get_float(self, key: ImGuiID, default_val: float = 0.0) -> float:          # imgui.h:2259
        pass
    def set_float(self, key: ImGuiID, val: float) -> None:                         # imgui.h:2260
        pass
    def get_void_ptr(self, key: ImGuiID) -> None:                                  # imgui.h:2261
        """ default_val is None"""
        pass
    def set_void_ptr(self, key: ImGuiID, val: None) -> None:                       # imgui.h:2262
        pass

    # - Get***Ref() functions finds pair, insert on demand if missing, return pointer. Useful if you intend to do Get+Set.
    # - References are only valid until a new value is added to the storage. Calling a Set***() function or a Get***Ref() function invalidates the pointer.
    # - A typical use case where this is convenient for quick hacking (e.g. add storage during a live Edit&Continue session if you can't modify existing struct)
    #      float* pvar = ImGui::GetFloatRef(key); ImGui::SliderFloat("var", pvar, 0, 100.0); some_var += *pvar;
    def get_int_ref(self, key: ImGuiID, default_val: int = 0) -> int:              # imgui.h:2268
        pass
    def get_bool_ref(self, key: ImGuiID, default_val: bool = False) -> bool:       # imgui.h:2269
        pass
    def get_float_ref(self, key: ImGuiID, default_val: float = 0.0) -> float:      # imgui.h:2270
        pass
    def get_void_ptr_ref(self, key: ImGuiID, default_val: None = None) -> None:    # imgui.h:2271
        pass

    def set_all_int(self, val: int) -> None:                                       # imgui.h:2274
        """ Use on your own storage if you know only integer are being stored (open/close all tree nodes)"""
        pass

    def build_sort_by_key(self) -> None:                                           # imgui.h:2277
        """ For quicker full rebuild of a storage (instead of an incremental one), you may add all your contents and then sort once."""
        pass

class ImGuiListClipper:    # imgui.h:2300
    """ Helper: Manually clip large list of items.
     If you have lots evenly spaced items and you have a random access to the list, you can perform coarse
     clipping based on visibility to only submit items that are in view.
     The clipper calculates the range of visible items and advance the cursor to compensate for the non-visible items we have skipped.
     (Dear ImGui already clip items based on their bounds but: it needs to first layout the item to do so, and generally
      fetching/submitting your own data incurs additional cost. Coarse clipping using ImGuiListClipper allows you to easily
      scale using lists with tens of thousands of items without a problem)
     Usage:
       ImGuiListClipper clipper;
       clipper.Begin(1000);         // We have 1000 elements, evenly spaced.
       while (clipper.Step())
           for (int i = clipper.DisplayStart; i < clipper.DisplayEnd; i++)
               ImGui::Text("line number %d", i);
     Generally what happens is:
     - Clipper lets you process the first element (DisplayStart = 0, DisplayEnd = 1) regardless of it being visible or not.
     - User code submit that one element.
     - Clipper can measure the height of the first element
     - Clipper calculate the actual range of elements to display based on the current clipping rectangle, position the cursor before the first visible element.
     - User code submit visible elements.
     - The clipper also handles various subtleties related to keyboard/gamepad navigation, wrapping etc.
    """
    display_start:int                                                                  # First item to display, updated by each call to Step()    # imgui.h:2302
    display_end:int                                                                    # End of items to display (exclusive)    # imgui.h:2303
    items_count:int                                                                    # [Internal] Number of items    # imgui.h:2304
    items_height:float                                                                 # [Internal] Height of item after a first step and item submission can calculate it    # imgui.h:2305
    start_pos_y:float                                                                  # [Internal] Cursor position at the time of Begin() or after table frozen rows are all processed    # imgui.h:2306
    temp_data:None                                                                     # [Internal] Internal data    # imgui.h:2307

    def __init__(self) -> None:                                                        # imgui.h:2311
        """ items_count: Use INT_MAX if you don't know how many items you have (in which case the cursor won't be advanced in the final step)
         items_height: Use -1.0 to be calculated automatically on first step. Otherwise pass in the distance between your items, typically GetTextLineHeightWithSpacing() or GetFrameHeightWithSpacing().
        """
        pass
    def begin(self, items_count: int, items_height: float = -1.0) -> None:             # imgui.h:2313
        pass
    def end(self) -> None:                                                             # imgui.h:2314
        """ Automatically called on the last call of Step() that returns False."""
        pass
    def step(self) -> bool:                                                            # imgui.h:2315
        """ Call until it returns False. The DisplayStart/DisplayEnd fields will be set and you can process/draw those items."""
        pass

    def force_display_range_by_indices(self, item_min: int, item_max: int) -> None:    # imgui.h:2318
        """ Call ForceDisplayRangeByIndices() before first call to Step() if you need a range of items to be displayed regardless of visibility."""
        pass
    # item_max is exclusive e.g. use (42, 42+1) to make item 42 always visible BUT due to alignment/padding of certain items it is likely that an extra item may be included on either end of the display range.


# Helpers macros to generate 32-bit encoded colors
# User can declare their own format by #defining the 5 _SHIFT/_MASK macros in their imconfig file.

class ImColor:    # imgui.h:2351
    """ Helper: ImColor() implicitly converts colors to either ImU32 (packed 4x1 byte) or ImVec4 (4x1 float)
     Prefer using IM_COL32() macros if you want a guaranteed compile-time ImU32 for usage with ImDrawList API.
     **Avoid storing ImColor! Store either u32 of ImVec4. This is not a full-featured color class. MAY OBSOLETE.
     **None of the ImGui API are using ImColor directly but you can use it as a convenience to pass colors in either ImU32 or ImVec4 formats. Explicitly cast to ImU32 or ImVec4 if needed.
    """
    value:ImVec4                                                                 # imgui.h:2353

    def __init__(self) -> None:                                                  # imgui.h:2355
        pass
    def __init__(self, r: float, g: float, b: float, a: float = 1.0) -> None:    # imgui.h:2356
        pass
    def __init__(self, col: ImVec4) -> None:                                     # imgui.h:2357
        pass
    def __init__(self, r: int, g: int, b: int, a: int = 255) -> None:            # imgui.h:2358
        pass
    def __init__(self, rgba: ImU32) -> None:                                     # imgui.h:2359
        pass

    # FIXME-OBSOLETE: May need to obsolete/cleanup those helpers.

#-----------------------------------------------------------------------------
# [SECTION] Drawing API (ImDrawCmd, ImDrawIdx, ImDrawVert, ImDrawChannel, ImDrawListSplitter, ImDrawListFlags, ImDrawList, ImDrawData)
# Hold a series of drawing commands. The user provides a renderer for ImDrawData which essentially contains an array of ImDrawList.
#-----------------------------------------------------------------------------

# The maximum line width to bake anti-aliased textures for. Build atlas with ImFontAtlasFlags_NoBakedLines to disable baking.

# ImDrawCallback: Draw callbacks for advanced uses [configurable type: override in imconfig.h]
# NB: You most likely do NOT need to use draw callbacks just to create your own widget or customized UI rendering,
# you can poke into the draw list for that! Draw callback may be useful for example to:
#  A) Change your GPU render state,
#  B) render a complex 3D scene inside a UI element without an intermediate texture/render target, etc.
# The expected behavior from your rendering function is 'if (cmd.UserCallback != None) { cmd.UserCallback(parent_list, cmd); } else { RenderTriangles() }'
# If you want to override the signature of ImDrawCallback, you can simply use e.g. '#define ImDrawCallback MyDrawCallback' (in imconfig.h) + update rendering backend accordingly.


class ImDrawCmd:    # imgui.h:2400
    """ Typically, 1 command = 1 GPU draw call (unless command is a callback)
     - VtxOffset: When 'io.BackendFlags & ImGuiBackendFlags_RendererHasVtxOffset' is enabled,
       this fields allow us to render meshes larger than 64K vertices while keeping 16-bit indices.
       Backends made for <1.71. will typically ignore the VtxOffset fields.
     - The ClipRect/TextureId/VtxOffset fields must be contiguous as we memcmp() them together (this is asserted for).
    """
    clip_rect:ImVec4               # 4*4  // Clipping rectangle (x1, y1, x2, y2). Subtract ImDrawData->DisplayPos to get clipping rectangle in "viewport" coordinates    # imgui.h:2402
    texture_id:ImTextureID         # 4-8  // User-provided texture ID. Set by user in ImfontAtlas::SetTexID() for fonts or passed to Image*() functions. Ignore if never using images or multiple fonts atlas.    # imgui.h:2403
    vtx_offset:int                 # 4    // Start offset in vertex buffer. ImGuiBackendFlags_RendererHasVtxOffset: always 0, otherwise may be >0 to support meshes larger than 64K vertices with 16-bit indices.    # imgui.h:2404
    idx_offset:int                 # 4    // Start offset in index buffer.    # imgui.h:2405
    elem_count:int                 # 4    // Number of indices (multiple of 3) to be rendered as triangles. Vertices are stored in the callee ImDrawList's vtx_buffer[] array, indices in idx_buffer[].    # imgui.h:2406
    user_callback_data:None        # 4-8  // The draw callback code can access this.    # imgui.h:2408

    def __init__(self) -> None:    # imgui.h:2410
        """ Also ensure our padding fields are zeroed"""
        pass


# Vertex layout

class ImDrawCmdHeader:    # imgui.h:2433
    """ [Internal] For use by ImDrawList"""
    clip_rect:ImVec4          # imgui.h:2435
    texture_id:ImTextureID    # imgui.h:2436
    vtx_offset:int            # imgui.h:2437

class ImDrawChannel:    # imgui.h:2441
    """ [Internal] For use by ImDrawListSplitter"""
    _cmd_buffer:List[ImDrawCmd]    # imgui.h:2443
    _idx_buffer:List[ImDrawIdx]    # imgui.h:2444


class ImDrawListSplitter:    # imgui.h:2450
    """ Split/Merge functions are used to split the draw list into different layers which can be drawn into out of order.
     This is used by the Columns/Tables API, so items of each column can be batched together in a same draw call.
    """
    _current:int                                                                       # Current channel number (0)    # imgui.h:2452
    _count:int                                                                         # Number of active channels (1+)    # imgui.h:2453
    _channels:List[ImDrawChannel]                                                      # Draw channels (not resized down so _Count might be < Channels.Size)    # imgui.h:2454

    def __init__(self) -> None:                                                        # imgui.h:2456
        pass
    def clear_free_memory(self) -> None:                                               # imgui.h:2459
        pass
    def split(self, draw_list: ImDrawList, count: int) -> None:                        # imgui.h:2460
        pass
    def merge(self, draw_list: ImDrawList) -> None:                                    # imgui.h:2461
        pass
    def set_current_channel(self, draw_list: ImDrawList, channel_idx: int) -> None:    # imgui.h:2462
        pass

class ImDrawFlags_(Enum):    # imgui.h:2467
    """ Flags for ImDrawList functions
     (Legacy: bit 0 must always correspond to ImDrawFlags_Closed to be backward compatible with old API using a bool. Bits 1..3 must be unused)
    """
    none = 0
    closed = 1 << 0                                                   # PathStroke(), AddPolyline(): specify that shape should be closed (Important: this is always == 1 for legacy reason)
    round_corners_top_left = 1 << 4                                   # AddRect(), AddRectFilled(), PathRect(): enable rounding top-left corner only (when rounding > 0.0, we default to all corners). Was 0x01.
    round_corners_top_right = 1 << 5                                  # AddRect(), AddRectFilled(), PathRect(): enable rounding top-right corner only (when rounding > 0.0, we default to all corners). Was 0x02.
    round_corners_bottom_left = 1 << 6                                # AddRect(), AddRectFilled(), PathRect(): enable rounding bottom-left corner only (when rounding > 0.0, we default to all corners). Was 0x04.
    round_corners_bottom_right = 1 << 7                               # AddRect(), AddRectFilled(), PathRect(): enable rounding bottom-right corner only (when rounding > 0.0, we default to all corners). Wax 0x08.
    round_corners_none = 1 << 8                                       # AddRect(), AddRectFilled(), PathRect(): disable rounding on all corners (when rounding > 0.0). This is NOT zero, NOT an implicit flag!
    round_corners_top = Literal[ImDrawFlags_.round_corners_top_left] | Literal[ImDrawFlags_.round_corners_top_right]
    round_corners_bottom = Literal[ImDrawFlags_.round_corners_bottom_left] | Literal[ImDrawFlags_.round_corners_bottom_right]
    round_corners_left = Literal[ImDrawFlags_.round_corners_bottom_left] | Literal[ImDrawFlags_.round_corners_top_left]
    round_corners_right = Literal[ImDrawFlags_.round_corners_bottom_right] | Literal[ImDrawFlags_.round_corners_top_right]
    round_corners_all = Literal[ImDrawFlags_.round_corners_top_left] | Literal[ImDrawFlags_.round_corners_top_right] | Literal[ImDrawFlags_.round_corners_bottom_left] | Literal[ImDrawFlags_.round_corners_bottom_right]
    round_corners_default_ = Literal[ImDrawFlags_.round_corners_all]  # Default to ALL corners if none of the _RoundCornersXX flags are specified.
    round_corners_mask_ = Literal[ImDrawFlags_.round_corners_all] | Literal[ImDrawFlags_.round_corners_none]

class ImDrawListFlags_(Enum):    # imgui.h:2487
    """ Flags for ImDrawList instance. Those are set automatically by ImGui:: functions from ImGuiIO settings, and generally not manipulated directly.
     It is however possible to temporarily alter flags between calls to ImDrawList:: functions.
    """
    none = 0
    anti_aliased_lines = 1 << 0          # Enable anti-aliased lines/borders (*2 the number of triangles for 1.0 wide line or lines thin enough to be drawn using textures, otherwise *3 the number of triangles)
    anti_aliased_lines_use_tex = 1 << 1  # Enable anti-aliased lines/borders using textures when possible. Require backend to render with bilinear filtering (NOT point/nearest filtering).
    anti_aliased_fill = 1 << 2           # Enable anti-aliased edge around filled shapes (rounded rectangles, circles).
    allow_vtx_offset = 1 << 3            # Can emit 'VtxOffset > 0' to allow large meshes. Set when 'ImGuiBackendFlags_RendererHasVtxOffset' is enabled.

class ImDrawList:    # imgui.h:2505
    """ Draw command list
     This is the low-level list of polygons that ImGui:: functions are filling. At the end of the frame,
     all command lists are passed to your ImGuiIO::RenderDrawListFn function for rendering.
     Each dear imgui window contains its own ImDrawList. You can use ImGui::GetWindowDrawList() to
     access the current window draw list and draw custom primitives.
     You can interleave normal ImGui:: calls and adding primitives to the current draw list.
     In single viewport mode, top-left is == GetMainViewport()->Pos (generally 0,0), bottom-right is == GetMainViewport()->Pos+Size (generally io.DisplaySize).
     You are totally free to apply whatever transformation matrix to want to the data (depending on the use of the transformation you may want to apply it to ClipRect as well!)
     Important: Primitives are always added to the list and not culled (culling is done at higher-level by ImGui:: functions), if you use this API a lot consider coarse culling your drawn objects.
    """
    # This is what you have to render
    cmd_buffer:List[ImDrawCmd]                                                        # Draw commands. Typically 1 command = 1 GPU draw call, unless the command is a callback.    # imgui.h:2508
    idx_buffer:List[ImDrawIdx]                                                        # Index buffer. Each command consume ImDrawCmd::ElemCount of those    # imgui.h:2509
    vtx_buffer:List[ImDrawVert]                                                       # Vertex buffer.    # imgui.h:2510
    flags:ImDrawListFlags                                                             # Flags, you may poke into these to adjust anti-aliasing settings per-primitive.    # imgui.h:2511

    # [Internal, used while building lists]
    _vtx_current_idx:int                                                              # [Internal] generally == VtxBuffer.Size unless we are past 64K vertices, in which case this gets reset to 0.    # imgui.h:2514
    _data:ImDrawListSharedData                                                        # Pointer to shared draw data (you can use ImGui::GetDrawListSharedData() to get the one from current ImGui context)    # imgui.h:2515
    _owner_name:str                                                                   # Pointer to owner window's name for debugging    # imgui.h:2516
    _vtx_write_ptr:ImDrawVert                                                         # [Internal] point within VtxBuffer.Data after each add command (to avoid using the ImVector<> operators too much)    # imgui.h:2517
    _idx_write_ptr:ImDrawIdx                                                          # [Internal] point within IdxBuffer.Data after each add command (to avoid using the ImVector<> operators too much)    # imgui.h:2518
    _clip_rect_stack:List[ImVec4]                                                     # [Internal]    # imgui.h:2519
    _texture_id_stack:List[ImTextureID]                                               # [Internal]    # imgui.h:2520
    _path:List[ImVec2]                                                                # [Internal] current path building    # imgui.h:2521
    _cmd_header:ImDrawCmdHeader                                                       # [Internal] template of active commands. Fields should match those of CmdBuffer.back().    # imgui.h:2522
    _splitter:ImDrawListSplitter                                                      # [Internal] for channels api (note: prefer using your own persistent instance of ImDrawListSplitter!)    # imgui.h:2523
    _fringe_scale:float                                                               # [Internal] anti-alias fringe is scaled by this value, this helps to keep things sharp while zooming at vertex buffer content    # imgui.h:2524

    def __init__(self, shared_data: ImDrawListSharedData) -> None:                    # imgui.h:2527
        """ If you want to create ImDrawList instances, pass them ImGui::GetDrawListSharedData() or create and use your own ImDrawListSharedData (so you can use ImDrawList without ImGui)"""
        pass

    def push_clip_rect(                                                               # imgui.h:2530
        self,
        clip_rect_min: ImVec2,
        clip_rect_max: ImVec2,
        intersect_with_current_clip_rect: bool = False
        ) -> None:
        """ Render-level scissoring. This is passed down to your render function but not used for CPU-side coarse clipping. Prefer using higher-level ImGui::PushClipRect() to affect logic (hit-testing and widget culling)"""
        pass
    def push_clip_rect_full_screen(self) -> None:                                     # imgui.h:2531
        pass
    def pop_clip_rect(self) -> None:                                                  # imgui.h:2532
        pass
    def push_texture_id(self, texture_id: ImTextureID) -> None:                       # imgui.h:2533
        pass
    def pop_texture_id(self) -> None:                                                 # imgui.h:2534
        pass

    # Primitives
    # - Filled shapes must always use clockwise winding order. The anti-aliasing fringe depends on it. Counter-clockwise shapes will have "inward" anti-aliasing.
    # - For rectangular primitives, "p_min" and "p_max" represent the upper-left and lower-right corners.
    # - For circle primitives, use "num_segments == 0" to automatically calculate tessellation (preferred).
    #   In older versions (until Dear ImGui 1.77) the AddCircle functions defaulted to num_segments == 12.
    #   In future versions we will use textures to provide cheaper and higher-quality circles.
    #   Use AddNgon() and AddNgonFilled() functions if you need to guaranteed a specific number of sides.
    def add_line(                                                                     # imgui.h:2545
        self,
        p1: ImVec2,
        p2: ImVec2,
        col: ImU32,
        thickness: float = 1.0
        ) -> None:
        pass
    def add_rect(                                                                     # imgui.h:2546
        self,
        p_min: ImVec2,
        p_max: ImVec2,
        col: ImU32,
        rounding: float = 0.0,
        flags: ImDrawFlags = 0,
        thickness: float = 1.0
        ) -> None:
        """ a: upper-left, b: lower-right (== upper-left + size)"""
        pass
    def add_rect_filled(                                                              # imgui.h:2547
        self,
        p_min: ImVec2,
        p_max: ImVec2,
        col: ImU32,
        rounding: float = 0.0,
        flags: ImDrawFlags = 0
        ) -> None:
        """ a: upper-left, b: lower-right (== upper-left + size)"""
        pass
    def add_rect_filled_multi_color(                                                  # imgui.h:2548
        self,
        p_min: ImVec2,
        p_max: ImVec2,
        col_upr_left: ImU32,
        col_upr_right: ImU32,
        col_bot_right: ImU32,
        col_bot_left: ImU32
        ) -> None:
        pass
    def add_quad(                                                                     # imgui.h:2549
        self,
        p1: ImVec2,
        p2: ImVec2,
        p3: ImVec2,
        p4: ImVec2,
        col: ImU32,
        thickness: float = 1.0
        ) -> None:
        pass
    def add_quad_filled(                                                              # imgui.h:2550
        self,
        p1: ImVec2,
        p2: ImVec2,
        p3: ImVec2,
        p4: ImVec2,
        col: ImU32
        ) -> None:
        pass
    def add_triangle(                                                                 # imgui.h:2551
        self,
        p1: ImVec2,
        p2: ImVec2,
        p3: ImVec2,
        col: ImU32,
        thickness: float = 1.0
        ) -> None:
        pass
    def add_triangle_filled(                                                          # imgui.h:2552
        self,
        p1: ImVec2,
        p2: ImVec2,
        p3: ImVec2,
        col: ImU32
        ) -> None:
        pass
    def add_circle(                                                                   # imgui.h:2553
        self,
        center: ImVec2,
        radius: float,
        col: ImU32,
        num_segments: int = 0,
        thickness: float = 1.0
        ) -> None:
        pass
    def add_circle_filled(                                                            # imgui.h:2554
        self,
        center: ImVec2,
        radius: float,
        col: ImU32,
        num_segments: int = 0
        ) -> None:
        pass
    def add_ngon(                                                                     # imgui.h:2555
        self,
        center: ImVec2,
        radius: float,
        col: ImU32,
        num_segments: int,
        thickness: float = 1.0
        ) -> None:
        pass
    def add_ngon_filled(                                                              # imgui.h:2556
        self,
        center: ImVec2,
        radius: float,
        col: ImU32,
        num_segments: int
        ) -> None:
        pass
    def add_text(                                                                     # imgui.h:2557
        self,
        pos: ImVec2,
        col: ImU32,
        text_begin: str,
        text_end: str = None
        ) -> None:
        pass
    def add_text(                                                                     # imgui.h:2558
        self,
        font: ImFont,
        font_size: float,
        pos: ImVec2,
        col: ImU32,
        text_begin: str,
        text_end: str = None,
        wrap_width: float = 0.0,
        cpu_fine_clip_rect: ImVec4 = None
        ) -> None:
        pass
    def add_polyline(                                                                 # imgui.h:2559
        self,
        points: ImVec2,
        num_points: int,
        col: ImU32,
        flags: ImDrawFlags,
        thickness: float
        ) -> None:
        pass
    def add_convex_poly_filled(                                                       # imgui.h:2560
        self,
        points: ImVec2,
        num_points: int,
        col: ImU32
        ) -> None:
        pass
    def add_bezier_cubic(                                                             # imgui.h:2561
        self,
        p1: ImVec2,
        p2: ImVec2,
        p3: ImVec2,
        p4: ImVec2,
        col: ImU32,
        thickness: float,
        num_segments: int = 0
        ) -> None:
        """ Cubic Bezier (4 control points)"""
        pass
    def add_bezier_quadratic(                                                         # imgui.h:2562
        self,
        p1: ImVec2,
        p2: ImVec2,
        p3: ImVec2,
        col: ImU32,
        thickness: float,
        num_segments: int = 0
        ) -> None:
        """ Quadratic Bezier (3 control points)"""
        pass

    # Image primitives
    # - Read FAQ to understand what ImTextureID is.
    # - "p_min" and "p_max" represent the upper-left and lower-right corners of the rectangle.
    # - "uv_min" and "uv_max" represent the normalized texture coordinates to use for those corners. Using (0,0)->(1,1) texture coordinates will generally display the entire texture.
    def add_image(                                                                    # imgui.h:2568
        self,
        user_texture_id: ImTextureID,
        p_min: ImVec2,
        p_max: ImVec2,
        uv_min: ImVec2 = ImVec2(0, 0),
        uv_max: ImVec2 = ImVec2(1, 1),
        col: ImU32 = IM_COL32_WHITE
        ) -> None:
        pass
    def add_image_quad(                                                               # imgui.h:2569
        self,
        user_texture_id: ImTextureID,
        p1: ImVec2,
        p2: ImVec2,
        p3: ImVec2,
        p4: ImVec2,
        uv1: ImVec2 = ImVec2(0, 0),
        uv2: ImVec2 = ImVec2(1, 0),
        uv3: ImVec2 = ImVec2(1, 1),
        uv4: ImVec2 = ImVec2(0, 1),
        col: ImU32 = IM_COL32_WHITE
        ) -> None:
        pass
    def add_image_rounded(                                                            # imgui.h:2570
        self,
        user_texture_id: ImTextureID,
        p_min: ImVec2,
        p_max: ImVec2,
        uv_min: ImVec2,
        uv_max: ImVec2,
        col: ImU32,
        rounding: float,
        flags: ImDrawFlags = 0
        ) -> None:
        pass

    # Stateful path API, add points then finish with PathFillConvex() or PathStroke()
    # - Filled shapes must always use clockwise winding order. The anti-aliasing fringe depends on it. Counter-clockwise shapes will have "inward" anti-aliasing.
    def path_arc_to(                                                                  # imgui.h:2579
        self,
        center: ImVec2,
        radius: float,
        a_min: float,
        a_max: float,
        num_segments: int = 0
        ) -> None:
        pass
    def path_arc_to_fast(                                                             # imgui.h:2580
        self,
        center: ImVec2,
        radius: float,
        a_min_of_12: int,
        a_max_of_12: int
        ) -> None:
        """ Use precomputed angles for a 12 steps circle"""
        pass
    def path_bezier_cubic_curve_to(                                                   # imgui.h:2581
        self,
        p2: ImVec2,
        p3: ImVec2,
        p4: ImVec2,
        num_segments: int = 0
        ) -> None:
        """ Cubic Bezier (4 control points)"""
        pass
    def path_bezier_quadratic_curve_to(                                               # imgui.h:2582
        self,
        p2: ImVec2,
        p3: ImVec2,
        num_segments: int = 0
        ) -> None:
        """ Quadratic Bezier (3 control points)"""
        pass
    def path_rect(                                                                    # imgui.h:2583
        self,
        rect_min: ImVec2,
        rect_max: ImVec2,
        rounding: float = 0.0,
        flags: ImDrawFlags = 0
        ) -> None:
        pass

    # Advanced
    def add_callback(self, callback: ImDrawCallback, callback_data: None) -> None:    # imgui.h:2586
        """ Your rendering function must check for 'UserCallback' in ImDrawCmd and call the function instead of rendering triangles."""
        pass
    def add_draw_cmd(self) -> None:                                                   # imgui.h:2587
        """ This is useful if you need to forcefully create a new draw call (to allow for dependent rendering / blending). Otherwise primitives are merged into the same draw-call as much as possible"""
        pass
    def clone_output(self) -> ImDrawList:                                             # imgui.h:2588
        """ Create a clone of the CmdBuffer/IdxBuffer/VtxBuffer."""
        pass

    # Advanced: Channels
    # - Use to split render into layers. By switching channels to can render out-of-order (e.g. submit FG primitives before BG primitives)
    # - Use to minimize draw calls (e.g. if going back-and-forth between multiple clipping rectangles, prefer to append into separate channels then merge at the end)
    # - FIXME-OBSOLETE: This API shouldn't have been in ImDrawList in the first place!
    #   Prefer using your own persistent instance of ImDrawListSplitter as you can stack them.
    #   Using the ImDrawList::ChannelsXXXX you cannot stack a split over another.

    # Advanced: Primitives allocations
    # - We render triangles (three vertices)
    # - All primitives needs to be reserved via PrimReserve() beforehand.
    def prim_reserve(self, idx_count: int, vtx_count: int) -> None:                   # imgui.h:2603
        pass
    def prim_unreserve(self, idx_count: int, vtx_count: int) -> None:                 # imgui.h:2604
        pass
    def prim_rect(self, a: ImVec2, b: ImVec2, col: ImU32) -> None:                    # imgui.h:2605
        """ Axis aligned rectangle (composed of two triangles)"""
        pass
    # Write vertex with unique index


    # [Internal helpers]
    def _reset_for_new_frame(self) -> None:                                           # imgui.h:2618
        pass
    def _clear_free_memory(self) -> None:                                             # imgui.h:2619
        pass
    def _pop_unused_draw_cmd(self) -> None:                                           # imgui.h:2620
        pass
    def _try_merge_draw_cmds(self) -> None:                                           # imgui.h:2621
        pass
    def _on_changed_clip_rect(self) -> None:                                          # imgui.h:2622
        pass
    def _on_changed_texture_id(self) -> None:                                         # imgui.h:2623
        pass
    def _on_changed_vtx_offset(self) -> None:                                         # imgui.h:2624
        pass
    def _calc_circle_auto_segment_count(self, radius: float) -> int:                  # imgui.h:2625
        pass
    def _path_arc_to_fast_ex(                                                         # imgui.h:2626
        self,
        center: ImVec2,
        radius: float,
        a_min_sample: int,
        a_max_sample: int,
        a_step: int
        ) -> None:
        pass
    def _path_arc_to_n(                                                               # imgui.h:2627
        self,
        center: ImVec2,
        radius: float,
        a_min: float,
        a_max: float,
        num_segments: int
        ) -> None:
        pass

class ImDrawData:    # imgui.h:2633
    """ All draw data to render a Dear ImGui frame
     (NB: the style and the naming convention here is a little inconsistent, we currently preserve them for backward compatibility purpose,
     as this is one of the oldest structure exposed by the library! Basically, ImDrawList == CmdList)
    """
    valid:bool                                               # Only valid after Render() is called and before the next NewFrame() is called.    # imgui.h:2635
    cmd_lists_count:int                                      # Number of ImDrawList* to render    # imgui.h:2636
    total_idx_count:int                                      # For convenience, sum of all ImDrawList's IdxBuffer.Size    # imgui.h:2637
    total_vtx_count:int                                      # For convenience, sum of all ImDrawList's VtxBuffer.Size    # imgui.h:2638
    display_pos:ImVec2                                       # Top-left position of the viewport to render (== top-left of the orthogonal projection matrix to use) (== GetMainViewport()->Pos for the main viewport, == (0.0) in most single-viewport applications)    # imgui.h:2640
    display_size:ImVec2                                      # Size of the viewport to render (== GetMainViewport()->Size for the main viewport, == io.DisplaySize in most single-viewport applications)    # imgui.h:2641
    framebuffer_scale:ImVec2                                 # Amount of pixels for each unit of DisplaySize. Based on io.DisplayFramebufferScale. Generally (1,1) on normal display, (2,2) on OSX with Retina display.    # imgui.h:2642

    def __init__(self) -> None:                              # imgui.h:2645
        """ Functions"""
        pass
    def de_index_all_buffers(self) -> None:                  # imgui.h:2647
        """ Helper to convert all buffers from indexed to non-indexed, in case you cannot render indexed. Note: this is slow and most likely a waste of resources. Always prefer indexed rendering!"""
        pass
    def scale_clip_rects(self, fb_scale: ImVec2) -> None:    # imgui.h:2648
        """ Helper to scale the ClipRect field of each ImDrawCmd. Use if your final output buffer is at a different scale than Dear ImGui expects, or if there is a difference between your window resolution and framebuffer resolution."""
        pass

#-----------------------------------------------------------------------------
# [SECTION] Font API (ImFontConfig, ImFontGlyph, ImFontAtlasFlags, ImFontAtlas, ImFontGlyphRangesBuilder, ImFont)
#-----------------------------------------------------------------------------

class ImFontConfig:    # imgui.h:2655
    font_data:None                 #          // TTF/OTF data    # imgui.h:2657
    font_data_size:int             #          // TTF/OTF data size    # imgui.h:2658
    font_data_owned_by_atlas:bool  # True     // TTF/OTF data ownership taken by the container ImFontAtlas (will delete memory itself).    # imgui.h:2659
    font_no:int                    # 0        // Index of font within TTF/OTF file    # imgui.h:2660
    size_pixels:float              #          // Size in pixels for rasterizer (more or less maps to the resulting font height).    # imgui.h:2661
    oversample_h:int               # 3        // Rasterize at higher quality for sub-pixel positioning. Note the difference between 2 and 3 is minimal so you can reduce this to 2 to save memory. Read https://github.com/nothings/stb/blob/master/tests/oversample/README.md for details.    # imgui.h:2662
    oversample_v:int               # 1        // Rasterize at higher quality for sub-pixel positioning. This is not really useful as we don't use sub-pixel positions on the Y axis.    # imgui.h:2663
    pixel_snap_h:bool              # False    // Align every glyph to pixel boundary. Useful e.g. if you are merging a non-pixel aligned font with the default font. If enabled, you can set OversampleH/V to 1.    # imgui.h:2664
    glyph_extra_spacing:ImVec2     # 0, 0     // Extra spacing (in pixels) between glyphs. Only X axis is supported for now.    # imgui.h:2665
    glyph_offset:ImVec2            # 0, 0     // Offset all glyphs from this font input.    # imgui.h:2666
    glyph_ranges:ImWchar           # None     // Pointer to a user-provided list of Unicode range (2 value per range, values are inclusive, zero-terminated list). THE ARRAY DATA NEEDS TO PERSIST AS LONG AS THE FONT IS ALIVE.    # imgui.h:2667
    glyph_min_advance_x:float      # 0        // Minimum AdvanceX for glyphs, set Min to align font icons, set both Min/Max to enforce mono-space font    # imgui.h:2668
    glyph_max_advance_x:float      # FLT_MAX  // Maximum AdvanceX for glyphs    # imgui.h:2669
    merge_mode:bool                # False    // Merge into previous ImFont, so you can combine multiple inputs font into one ImFont (e.g. ASCII font + icons + Japanese glyphs). You may want to use GlyphOffset.y when merge font of different heights.    # imgui.h:2670
    font_builder_flags:int         # 0        // Settings for custom font builder. THIS IS BUILDER IMPLEMENTATION DEPENDENT. Leave as zero if unsure.    # imgui.h:2671
    rasterizer_multiply:float      # 1.0     // Brighten (>1.0) or darken (<1.0) font output. Brightening small fonts may be a good workaround to make them more readable.    # imgui.h:2672
    ellipsis_char:ImWchar          # -1       // Explicitly specify unicode codepoint of ellipsis character. When fonts are being merged first specified ellipsis will be used.    # imgui.h:2673

    # [Internal]
    dst_font:ImFont                # imgui.h:2677

    def __init__(self) -> None:    # imgui.h:2679
        pass

class ImFontGlyph:    # imgui.h:2684
    """ Hold rendering data for one glyph.
     (Note: some language parsers may fail to convert the 31+1 bitfield members, in this case maybe drop store a single u32 or we can rework this)
    """
    advance_x:float  # Distance to next character (= data from font + ImFontConfig::GlyphExtraSpacing.x baked in)    # imgui.h:2689
    x0:float         # Glyph corners    # imgui.h:2690
    y0:float         # Glyph corners    # imgui.h:2690
    x1:float         # Glyph corners    # imgui.h:2690
    y1:float         # Glyph corners    # imgui.h:2690
    u0:float         # Texture coordinates    # imgui.h:2691
    v0:float         # Texture coordinates    # imgui.h:2691
    u1:float         # Texture coordinates    # imgui.h:2691
    v1:float         # Texture coordinates    # imgui.h:2691

class ImFontGlyphRangesBuilder:    # imgui.h:2696
    """ Helper to build glyph ranges from text/string data. Feed your application strings/characters to it then call BuildRanges().
     This is essentially a tightly packed of vector of 64k booleans = 8KB storage.
    """
    used_chars:List[ImU32]                                          # Store 1-bit per Unicode code point (0=unused, 1=used)    # imgui.h:2698

    def __init__(self) -> None:                                     # imgui.h:2700
        pass
    def add_text(self, text: str, text_end: str = None) -> None:    # imgui.h:2705
        """ Add string (each character of the UTF-8 string are added)"""
        pass
    def add_ranges(self, ranges: ImWchar) -> None:                  # imgui.h:2706
        """ Add ranges, e.g. builder.AddRanges(ImFontAtlas::GetGlyphRangesDefault()) to force add all of ASCII/Latin+Ext"""
        pass
    def build_ranges(self, out_ranges: List[ImWchar]) -> None:      # imgui.h:2707
        """ Output new ranges"""
        pass

class ImFontAtlasCustomRect:    # imgui.h:2711
    """ See ImFontAtlas::AddCustomRectXXX functions."""
    width:int                      # Input    // Desired rectangle dimension    # imgui.h:2713
    height:int                     # Input    // Desired rectangle dimension    # imgui.h:2713
    x:int                          # Output   // Packed position in Atlas    # imgui.h:2714
    y:int                          # Output   // Packed position in Atlas    # imgui.h:2714
    glyph_id:int                   # Input    // For custom font glyphs only (ID < 0x110000)    # imgui.h:2715
    glyph_advance_x:float          # Input    // For custom font glyphs only: glyph xadvance    # imgui.h:2716
    glyph_offset:ImVec2            # Input    // For custom font glyphs only: glyph display offset    # imgui.h:2717
    font:ImFont                    # Input    // For custom font glyphs only: target font    # imgui.h:2718
    def __init__(self) -> None:    # imgui.h:2719
        pass

class ImFontAtlasFlags_(Enum):    # imgui.h:2724
    """ Flags for ImFontAtlas build"""
    none = 0
    no_power_of_two_height = 1 << 0  # Don't round the height to next power of two
    no_mouse_cursors = 1 << 1        # Don't build software mouse cursors into the atlas (save a little texture memory)
    no_baked_lines = 1 << 2          # Don't build thick line textures into the atlas (save a little texture memory, allow support for point/nearest filtering). The AntiAliasedLinesUseTex features uses them, otherwise they will be rendered using polygons (more expensive for CPU/GPU).

class ImFontAtlas:    # imgui.h:2749
    """ Load and rasterize multiple TTF/OTF fonts into a same texture. The font atlas will build a single texture holding:
      - One or more fonts.
      - Custom graphics data needed to render the shapes needed by Dear ImGui.
      - Mouse cursor shapes for software cursor rendering (unless setting 'Flags |= ImFontAtlasFlags_NoMouseCursors' in the font atlas).
     It is the user-code responsibility to setup/build the atlas, then upload the pixel data into a texture accessible by your graphics api.
      - Optionally, call any of the AddFont*** functions. If you don't call any, the default font embedded in the code will be loaded for you.
      - Call GetTexDataAsAlpha8() or GetTexDataAsRGBA32() to build and retrieve pixels data.
      - Upload the pixels data into a texture within your graphics system (see imgui_impl_xxxx.cpp examples)
      - Call SetTexID(my_tex_id); and pass the pointer/identifier to your texture in a format natural to your graphics API.
        This value will be passed back to you during rendering to identify the texture. Read FAQ entry about ImTextureID for more details.
     Common pitfalls:
     - If you pass a 'glyph_ranges' array to AddFont*** functions, you need to make sure that your array persist up until the
       atlas is build (when calling GetTexData*** or Build()). We only copy the pointer, not the data.
     - Important: By default, AddFontFromMemoryTTF() takes ownership of the data. Even though we are not writing to it, we will free the pointer on destruction.
       You can set font_cfg->FontDataOwnedByAtlas=False to keep ownership of your data and it won't be freed,
     - Even though many functions are suffixed with "TTF", OTF data is supported just as well.
     - This is an old API and it is currently awkward for those and and various other reasons! We will address them in the future!
    """
    def __init__(self) -> None:                                             # imgui.h:2751
        pass
    def add_font(self, font_cfg: ImFontConfig) -> ImFont:                   # imgui.h:2753
        pass
    def add_font_default(self, font_cfg: ImFontConfig = None) -> ImFont:    # imgui.h:2754
        pass
    def add_font_from_file_ttf(                                             # imgui.h:2755
        self,
        filename: str,
        size_pixels: float,
        font_cfg: ImFontConfig = None,
        glyph_ranges: ImWchar = None
        ) -> ImFont:
        pass
    def add_font_from_memory_ttf(                                           # imgui.h:2756
        self,
        font_data: None,
        font_size: int,
        size_pixels: float,
        font_cfg: ImFontConfig = None,
        glyph_ranges: ImWchar = None
        ) -> ImFont:
        """ Note: Transfer ownership of 'ttf_data' to ImFontAtlas! Will be deleted after destruction of the atlas. Set font_cfg->FontDataOwnedByAtlas=False to keep ownership of your data and it won't be freed."""
        pass
    def add_font_from_memory_compressed_ttf(                                # imgui.h:2757
        self,
        compressed_font_data: None,
        compressed_font_size: int,
        size_pixels: float,
        font_cfg: ImFontConfig = None,
        glyph_ranges: ImWchar = None
        ) -> ImFont:
        """ 'compressed_font_data' still owned by caller. Compress with binary_to_compressed_c.cpp."""
        pass
    def add_font_from_memory_compressed_base85_ttf(                         # imgui.h:2758
        self,
        compressed_font_data_base85: str,
        size_pixels: float,
        font_cfg: ImFontConfig = None,
        glyph_ranges: ImWchar = None
        ) -> ImFont:
        """ 'compressed_font_data_base85' still owned by caller. Compress with binary_to_compressed_c.cpp with -base85 parameter."""
        pass
    def clear_input_data(self) -> None:                                     # imgui.h:2759
        """ Clear input data (all ImFontConfig structures including sizes, TTF data, glyph ranges, etc.) = all the data used to build the texture and fonts."""
        pass
    def clear_tex_data(self) -> None:                                       # imgui.h:2760
        """ Clear output texture data (CPU side). Saves RAM once the texture has been copied to graphics memory."""
        pass
    def clear_fonts(self) -> None:                                          # imgui.h:2761
        """ Clear output font data (glyphs storage, UV coordinates)."""
        pass
    def clear(self) -> None:                                                # imgui.h:2762
        """ Clear all input and output."""
        pass

    # Build atlas, retrieve pixel data.
    # User is in charge of copying the pixels into graphics memory (e.g. create a texture with your engine). Then store your texture handle with SetTexID().
    # The pitch is always = Width * BytesPerPixels (1 or 4)
    # Building in RGBA32 format is provided for convenience and compatibility, but note that unless you manually manipulate or copy color data into
    # the texture (e.g. when using the AddCustomRect*** api), then the RGB pixels emitted will always be white (~75% of memory/bandwidth waste.
    def build(self) -> bool:                                                # imgui.h:2769
        """ Build pixels data. This is called automatically for you by the GetTexData*** functions."""
        pass

    #-------------------------------------------
    # Glyph Ranges
    #-------------------------------------------

    # Helpers to retrieve list of common Unicode ranges (2 value per range, values are inclusive, zero-terminated list)
    # NB: Make sure that your string are UTF-8 and NOT in your local code page. In C++11, you can create UTF-8 string literal using the u8"Hello world" syntax. See FAQ for details.
    # NB: Consider using ImFontGlyphRangesBuilder to build glyph ranges from textual data.
    def get_glyph_ranges_default(self) -> ImWchar:                          # imgui.h:2782
        """ Basic Latin, Extended Latin"""
        pass
    def get_glyph_ranges_korean(self) -> ImWchar:                           # imgui.h:2783
        """ Default + Korean characters"""
        pass
    def get_glyph_ranges_japanese(self) -> ImWchar:                         # imgui.h:2784
        """ Default + Hiragana, Katakana, Half-Width, Selection of 2999 Ideographs"""
        pass
    def get_glyph_ranges_chinese_full(self) -> ImWchar:                     # imgui.h:2785
        """ Default + Half-Width + Japanese Hiragana/Katakana + full set of about 21000 CJK Unified Ideographs"""
        pass
    def get_glyph_ranges_chinese_simplified_common(self) -> ImWchar:        # imgui.h:2786
        """ Default + Half-Width + Japanese Hiragana/Katakana + set of 2500 CJK Unified Ideographs for common simplified Chinese"""
        pass
    def get_glyph_ranges_cyrillic(self) -> ImWchar:                         # imgui.h:2787
        """ Default + about 400 Cyrillic characters"""
        pass
    def get_glyph_ranges_thai(self) -> ImWchar:                             # imgui.h:2788
        """ Default + Thai characters"""
        pass
    def get_glyph_ranges_vietnamese(self) -> ImWchar:                       # imgui.h:2789
        """ Default + Vietnamese characters"""
        pass

    #-------------------------------------------
    # [BETA] Custom Rectangles/Glyphs API
    #-------------------------------------------

    # You can request arbitrary rectangles to be packed into the atlas, for your own purposes.
    # - After calling Build(), you can query the rectangle position and render your pixels.
    # - If you render colored output, set 'atlas->TexPixelsUseColors = True' as this may help some backends decide of prefered texture format.
    # - You can also request your rectangles to be mapped as font glyph (given a font + Unicode point),
    #   so you can render e.g. custom colorful icons and use them as regular glyphs.
    # - Read docs/FONTS.md for more details about using colorful icons.
    # - Note: this API may be redesigned later in order to support multi-monitor varying DPI settings.
    def add_custom_rect_regular(self, width: int, height: int) -> int:      # imgui.h:2802
        pass
    def add_custom_rect_font_glyph(                                         # imgui.h:2803
        self,
        font: ImFont,
        id: ImWchar,
        width: int,
        height: int,
        advance_x: float,
        offset: ImVec2 = ImVec2(0, 0)
        ) -> int:
        pass

    # [Internal]
    def get_mouse_cursor_tex_data(                                          # imgui.h:2808
        self,
        cursor: ImGuiMouseCursor,
        out_offset: ImVec2,
        out_size: ImVec2,
        out_uv_border_0: ImVec2,
        out_uv_border_1: ImVec2,
        out_uv_fill_0: ImVec2,
        out_uv_fill_1: ImVec2
        ) -> bool:
        pass

    #-------------------------------------------
    # Members
    #-------------------------------------------

    flags:ImFontAtlasFlags                                                  # Build flags (see ImFontAtlasFlags_)    # imgui.h:2814
    tex_id:ImTextureID                                                      # User data to refer to the texture once it has been uploaded to user's graphic systems. It is passed back to you during rendering via the ImDrawCmd structure.    # imgui.h:2815
    tex_desired_width:int                                                   # Texture width desired by user before Build(). Must be a power-of-two. If have many glyphs your graphics API have texture size restrictions you may want to increase texture width to decrease height.    # imgui.h:2816
    tex_glyph_padding:int                                                   # Padding between glyphs within texture in pixels. Defaults to 1. If your rendering method doesn't rely on bilinear filtering you may set this to 0 (will also need to set AntiAliasedLinesUseTex = False).    # imgui.h:2817
    locked:bool                                                             # Marked as Locked by ImGui::NewFrame() so attempt to modify the atlas will assert.    # imgui.h:2818

    # [Internal]
    # NB: Access texture data via GetTexData*() calls! Which will setup a default font for you.
    tex_ready:bool                                                          # Set when texture was built matching current font input    # imgui.h:2822
    tex_pixels_use_colors:bool                                              # Tell whether our texture data is known to use colors (rather than just alpha channel), in order to help backend select a format.    # imgui.h:2823
    tex_pixels_alpha8:unsigned char                                         # 1 component per pixel, each component is unsigned 8-bit. Total size = TexWidth * TexHeight    # imgui.h:2824
    tex_pixels_rgba32:int                                                   # 4 component per pixel, each component is unsigned 8-bit. Total size = TexWidth * TexHeight * 4    # imgui.h:2825
    tex_width:int                                                           # Texture width calculated during Build().    # imgui.h:2826
    tex_height:int                                                          # Texture height calculated during Build().    # imgui.h:2827
    tex_uv_scale:ImVec2                                                     # = (1.0/TexWidth, 1.0/TexHeight)    # imgui.h:2828
    tex_uv_white_pixel:ImVec2                                               # Texture coordinates to a white pixel    # imgui.h:2829
    fonts:List[ImFont]                                                      # Hold all the fonts returned by AddFont*. Fonts[0] is the default font upon calling ImGui::NewFrame(), use ImGui::PushFont()/PopFont() to change the current font.    # imgui.h:2830
    custom_rects:List[ImFontAtlasCustomRect]                                # Rectangles for packing custom texture data into the atlas.    # imgui.h:2831
    config_data:List[ImFontConfig]                                          # Configuration data    # imgui.h:2832

    # [Internal] Font builder
    font_builder_io:ImFontBuilderIO                                         # Opaque interface to a font builder (default to stb_truetype, can be changed to use FreeType by defining IMGUI_ENABLE_FREETYPE).    # imgui.h:2836
    font_builder_flags:int                                                  # Shared flags (for all fonts) for custom font builder. THIS IS BUILD IMPLEMENTATION DEPENDENT. Per-font override is also available in ImFontConfig.    # imgui.h:2837

    # [Internal] Packing data
    pack_id_mouse_cursors:int                                               # Custom texture rectangle ID for white pixel and mouse cursors    # imgui.h:2840
    pack_id_lines:int                                                       # Custom texture rectangle ID for baked anti-aliased lines    # imgui.h:2841

    # [Obsolete]
    #typedef ImFontAtlasCustomRect    CustomRect;         // OBSOLETED in 1.72+
    #typedef ImFontGlyphRangesBuilder GlyphRangesBuilder; // OBSOLETED in 1.67+

class ImFont:    # imgui.h:2850
    """ Font runtime data and rendering
     ImFontAtlas automatically loads a default embedded font for you when you call GetTexDataAsAlpha8() or GetTexDataAsRGBA32().
    """
    # Members: Hot ~20/24 bytes (for CalcTextSize)
    index_advance_x:List[float]                                            # 12-16 // out //            // Sparse. Glyphs->AdvanceX in a directly indexable way (cache-friendly for CalcTextSize functions which only this this info, and are often bottleneck in large UI).    # imgui.h:2853
    fallback_advance_x:float                                               # 4     // out // = FallbackGlyph->AdvanceX    # imgui.h:2854
    font_size:float                                                        # 4     // in  //            // Height of characters/line, set during loading (don't change after loading)    # imgui.h:2855

    # Members: Hot ~28/40 bytes (for CalcTextSize + render loop)
    index_lookup:List[ImWchar]                                             # 12-16 // out //            // Sparse. Index glyphs by Unicode code-point.    # imgui.h:2858
    glyphs:List[ImFontGlyph]                                               # 12-16 // out //            // All glyphs.    # imgui.h:2859
    fallback_glyph:ImFontGlyph                                             # 4-8   // out // = FindGlyph(FontFallbackChar)    # imgui.h:2860

    # Members: Cold ~32/40 bytes
    container_atlas:ImFontAtlas                                            # 4-8   // out //            // What we has been loaded into    # imgui.h:2863
    config_data:ImFontConfig                                               # 4-8   // in  //            // Pointer within ContainerAtlas->ConfigData    # imgui.h:2864
    config_data_count:int                                                  # 2     // in  // ~ 1        // Number of ImFontConfig involved in creating this font. Bigger than 1 when merging multiple font sources into one ImFont.    # imgui.h:2865
    fallback_char:ImWchar                                                  # 2     // out // = FFFD/'?' // Character used if a glyph isn't found.    # imgui.h:2866
    ellipsis_char:ImWchar                                                  # 2     // out // = '...'    // Character used for ellipsis rendering.    # imgui.h:2867
    dot_char:ImWchar                                                       # 2     // out // = '.'      // Character used for ellipsis rendering (if a single '...' character isn't found)    # imgui.h:2868
    dirty_lookup_tables:bool                                               # 1     // out //    # imgui.h:2869
    scale:float                                                            # 4     // in  // = 1.      // Base font scale, multiplied by the per-window font scale which you can adjust with SetWindowFontScale()    # imgui.h:2870
    ascent:float                                                           # 4+4   // out //            // Ascent: distance from top to bottom of e.g. 'A' [0..FontSize]    # imgui.h:2871
    descent:float                                                          # 4+4   // out //            // Ascent: distance from top to bottom of e.g. 'A' [0..FontSize]    # imgui.h:2871
    metrics_total_surface:int                                              # 4     // out //            // Total surface in pixels to get an idea of the font rasterization/texture cost (not exact, we approximate the cost of padding between glyphs)    # imgui.h:2872

    def __init__(self) -> None:                                            # imgui.h:2876
        """ Methods"""
        pass
    def find_glyph(self, c: ImWchar) -> ImFontGlyph:                       # imgui.h:2878
        pass
    def find_glyph_no_fallback(self, c: ImWchar) -> ImFontGlyph:           # imgui.h:2879
        pass

    # 'max_width' stops rendering after a certain width (could be turned into a 2 size). FLT_MAX to disable.
    # 'wrap_width' enable automatic word-wrapping across multiple lines to fit into given width. 0.0 to disable.
    def calc_word_wrap_position_a(                                         # imgui.h:2887
        self,
        scale: float,
        text: str,
        text_end: str,
        wrap_width: float
        ) -> str:
        pass
    def render_char(                                                       # imgui.h:2888
        self,
        draw_list: ImDrawList,
        size: float,
        pos: ImVec2,
        col: ImU32,
        c: ImWchar
        ) -> None:
        pass
    def render_text(                                                       # imgui.h:2889
        self,
        draw_list: ImDrawList,
        size: float,
        pos: ImVec2,
        col: ImU32,
        clip_rect: ImVec4,
        text_begin: str,
        text_end: str,
        wrap_width: float = 0.0,
        cpu_fine_clip: bool = False
        ) -> None:
        pass

    # [Internal] Don't use!
    def build_lookup_table(self) -> None:                                  # imgui.h:2892
        pass
    def clear_output_data(self) -> None:                                   # imgui.h:2893
        pass
    def grow_index(self, new_size: int) -> None:                           # imgui.h:2894
        pass
    def add_glyph(                                                         # imgui.h:2895
        self,
        src_cfg: ImFontConfig,
        c: ImWchar,
        x0: float,
        y0: float,
        x1: float,
        y1: float,
        u0: float,
        v0: float,
        u1: float,
        v1: float,
        advance_x: float
        ) -> None:
        pass
    def add_remap_char(                                                    # imgui.h:2896
        self,
        dst: ImWchar,
        src: ImWchar,
        overwrite_dst: bool = True
        ) -> None:
        """ Makes 'dst' character/glyph points to 'src' character/glyph. Currently needs to be called AFTER fonts have been built."""
        pass
    def set_glyph_visible(self, c: ImWchar, visible: bool) -> None:        # imgui.h:2897
        pass
    def is_glyph_range_unused(self, c_begin: int, c_last: int) -> bool:    # imgui.h:2898
        pass

#-----------------------------------------------------------------------------
# [SECTION] Viewports
#-----------------------------------------------------------------------------

class ImGuiViewportFlags_(Enum):    # imgui.h:2906
    """ Flags stored in ImGuiViewport::Flags, giving indications to the platform backends."""
    none = 0
    is_platform_window = 1 << 0   # Represent a Platform Window
    is_platform_monitor = 1 << 1  # Represent a Platform Monitor (unused yet)
    owned_by_app = 1 << 2         # Platform Window: is created/managed by the application (rather than a dear imgui backend)

class ImGuiViewport:    # imgui.h:2921
    """ - Currently represents the Platform Window created by the application which is hosting our Dear ImGui windows.
     - In 'docking' branch with multi-viewport enabled, we extend this concept to have multiple active viewports.
     - In the future we will extend this concept further to also represent Platform Monitor and support a "no main platform window" operation mode.
     - About Main Area vs Work Area:
       - Main Area = entire viewport.
       - Work Area = entire viewport minus sections used by main menu bars (for platform windows), or by task bar (for platform monitor).
       - Windows are generally trying to stay within the Work Area of their host viewport.
    """
    flags:ImGuiViewportFlags       # See ImGuiViewportFlags_    # imgui.h:2923
    pos:ImVec2                     # Main Area: Position of the viewport (Dear ImGui coordinates are the same as OS desktop/native coordinates)    # imgui.h:2924
    size:ImVec2                    # Main Area: Size of the viewport.    # imgui.h:2925
    work_pos:ImVec2                # Work Area: Position of the viewport minus task bars, menus bars, status bars (>= Pos)    # imgui.h:2926
    work_size:ImVec2               # Work Area: Size of the viewport minus task bars, menu bars, status bars (<= Size)    # imgui.h:2927

    # Platform/Backend Dependent Data
    platform_handle_raw:None       # None* to hold lower-level, platform-native window handle (under Win32 this is expected to be a HWND, unused for other platforms)    # imgui.h:2930

    def __init__(self) -> None:    # imgui.h:2932
        pass

    # Helpers

#-----------------------------------------------------------------------------
# [SECTION] Platform Dependent Interfaces
#-----------------------------------------------------------------------------

class ImGuiPlatformImeData:    # imgui.h:2944
    """ (Optional) Support for IME (Input Method Editor) via the io.SetPlatformImeDataFn() function."""
    want_visible:bool              # A widget wants the IME to be visible    # imgui.h:2946
    input_pos:ImVec2               # Position of the input cursor    # imgui.h:2947
    input_line_height:float        # Line height    # imgui.h:2948

    def __init__(self) -> None:    # imgui.h:2950
        pass

#-----------------------------------------------------------------------------
# [SECTION] Obsolete functions and types
# (Will be removed! Read 'API BREAKING CHANGES' section in imgui.cpp for details)
# Please keep your copy of dear imgui up to date! Occasionally set '#define IMGUI_DISABLE_OBSOLETE_FUNCTIONS' in imconfig.h to stay ahead.
#-----------------------------------------------------------------------------

# <Namespace ImGui>
# </Namespace ImGui>


#-----------------------------------------------------------------------------



# Include imgui_user.h at the end of imgui.h (convenient for user to only explicitly include vanilla imgui.h)


# </litgen_stub>

# fmt: on
