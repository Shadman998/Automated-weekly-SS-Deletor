# Automated-weekly-SS-Deletor

A lightweight Python utility designed for "digital housekeeping." Instead of manually clearing out your screenshots folder, this script acts as a smart sieve, automatically identifying and removing files older than 7 days while keeping your recent work safe.🧠 The IntuitionUnlike a "sledgehammer" approach that wipes an entire folder, this script uses file metadata.


It checks the "Last Modified" timestamp st.mtime of every file.

If: 
{Current Time}-{File Modified Time} > 7 days,
The file is permanently removed to save storage.
🛠️ FeaturesSafety Buffer: Keeps the last 7 days of screenshots so you don't lose active work.
Error Handling: Skips files that are currently open or system-protected.Path Resilience: Uses pathlib for modern, cross-platform path handling.Background Ready: Compatible with pythonw.exe for invisible execution.

🚀 Setup & Installation:-
Prerequisites:
1.Python 3.12+ (Developed and tested on Python 3.12).
2.Windows Task Scheduler (for automation).
3.ConfigurationOpen automated_ss_deletor.py and update the SS_FOLDER_PATH variable.
Important: Use a raw string (prefix with r) to avoid Windows path errors:PythonSS_FOLDER_PATH = r"C:\Users\USER\Pictures\Screenshots"

Automation (Windows)To truly "set it and forget it," schedule the script to run weekly:Open Task Scheduler > Create Basic Task.Trigger: Weekly (e.g., Every Saturday at 9:00 PM).Action: Start a Program.Program/Script: C:\Path\To\Your\pythonw.exeAdd Arguments: "D:\automated_ss_deletor.py"⚠️ Safety NoteThis script uses file_path.unlink(), which bypasses the Recycle Bin. It is highly recommended to perform a "Dry Run" by commenting out the delete line and using print() to verify which files will be removed before final deployment.
