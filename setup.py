from setuptools import find_packages, setup

setup(
    name="multi-domain-lexicon",
    version="0.1.0",
    description=(
        "Deterministic lexicographical taxonomy, visual reference grounding, "
        "incremental GraphRAG token-offset calculator, and prompt compiler across "
        "ArtCraft creative apps, Graphic Engineering, Architectural Design Thinking, "
        "Physical Fabrication, AI, and Quantum Computing."
    ),
    author="NoJuanNobody",
    packages=find_packages(exclude=["tests*"]),
    python_requires=">=3.9",
    entry_points={
        "console_scripts": [
            "multi-domain-lexicon = multi_domain_lexicon.cli:main",
        ],
    },
)
