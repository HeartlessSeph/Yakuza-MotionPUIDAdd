# Yakuza-MotionPUIDAdd
A command line tool that adds entries to a motion puid file extracted with Retraso's reARMP based on files in a folder.

Usage:
Before starting, extract motion_gmt.bin and/or motion_bep.bin from PUID (or motion.par for Yakuza 6) and extract them to json using Retraso's reARMP: https://github.com/CapitanRetraso/reARMP/releases/

-bep for the extracted bep json

-gmt for the extracted gmt json

-d for the directory containing gmt (or gmt.lexus2 for Kiwami 2) and/or bep (or bep.lexus2 for Kiwami 2)

Either -bep or -gmt should be defined before running though only one of them is required. -d is required to run the program. After running the program will show any entries that are duplicates and indicate that they were skipped to prevent duplicate PUID entries. All new entries will be added and placed in the file.
