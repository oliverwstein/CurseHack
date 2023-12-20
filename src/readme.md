CurseHack/
│
├── src/                     # Main source files
│   ├── actions/             # Action-related classes
│   │   ├── ActionManager.ts
│   │   ├── Move.ts
│   │   ├── Open.ts
│   │   └── ...              # Other action subclasses
│   │
│   ├── data/                # Data files for game content
│   │   ├── monsterData.ts
│   │   ├── featureData.ts
│   │   └── ...              # Other data files
│   │
│   ├── entities/            # Game entities like player, monsters
│   │   ├── Player.ts
│   │   ├── MonsterManager.ts
│   │   └── ...              # Other entity-related classes
│   │
│   ├── levels/              # Level management and components
│   │   ├── LevelManager.ts
│   │   ├── Room.ts
│   │   └── ...              # Other level-related classes
│   │
│   ├── tiles/               # Tile-related classes
│   │   ├── Tile.ts
│   │   └── ...              # Other tile subclasses
│   │
│   ├── utils/               # Utility functions and classes
│   │   └── ...              # Utility files
│   │
│   ├── Game.ts              # Core game controller class
│   ├── main.ts              # Entry point of the game
│   └── index.ts             # Main module export file
│
├── assets/                  # Static assets like images, sounds
│   └── ...
│
├── dist/                    # Compiled JavaScript files
│   └── ...
│
├── node_modules/            # Node modules (not tracked in version control)
│   └── ...
│
├── package.json             # Project metadata and dependencies
├── tsconfig.json            # TypeScript configuration file
└── README.md                # Project overview and documentation
