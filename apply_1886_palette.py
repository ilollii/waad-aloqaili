import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace hardcoded legacy dark purple backgrounds and borders with sleek 1886 Riyadh luxury black / neutral grays
replacements = [
    # Dark purples -> Sleek rich blacks
    ('#2C1A48', '#0A0A0A'),
    ('#1A0D2E', '#141414'),
    ('#120820', '#0A0A0A'),
    ('#140B24', '#0A0A0A'),
    ('#1B0F30', '#121212'),
    ('#23143D', '#1A1A1A'),
    ('#321E52', '#262626'),
    ('#4A2F75', '#333333'),
    ('#553488', '#333333'),
    ('#432468', '#1A1A1A'),
    ('#58496E', '#4B5563'),
    ('#8E7D9F', '#8E8E93'),
    ('#9E8DB3', '#9CA3AF'),
    ('#D4C6E5', '#D1D5DB'),
    ('#ECE4F7', '#ECECEF'),
    ('#F7F3FB', '#F4F4F6'),
    ('#F8F5FC', '#F9FAFB'),
    ('#F3EDF9', '#F4F4F6'),
    ('#E8E0F2', '#E5E7EB'),
    ('#DCD0EE', '#E0E0E6'),
    ('rgba(44, 26, 72,', 'rgba(0, 0, 0,'),
    ('rgba(18, 8, 32,', 'rgba(10, 10, 10,'),
    ('rgba(26, 13, 46,', 'rgba(20, 20, 20,'),
    ('rgba(220, 208, 238,', 'rgba(229, 231, 235,'),
]

for old_val, new_val in replacements:
    css = css.replace(old_val, new_val)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated styles.css with 1886 Riyadh luxury aesthetic (Black, White, Neutral Grays)")
