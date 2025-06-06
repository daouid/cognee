"""Data models for the cognitive architecture."""

from enum import Enum, auto
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, Field
from cognee.infrastructure.llm.config import get_llm_config

if get_llm_config().llm_provider.lower() == "gemini":
    """
    Note: Gemini doesn't allow for an empty dictionary to be a part of the data model
    so we created new data models to bypass that issue, but other LLMs have slightly worse performance
    when creating knowledge graphs with these data models compared to the old data models
    so now there's an if statement here so that the rest of the LLMs can use the old data models.
    """

    class Node(BaseModel):
        """Node in a knowledge graph."""

        id: str
        name: str
        type: str
        description: str
        label: str

    class Edge(BaseModel):
        """Edge in a knowledge graph."""

        source_node_id: str
        target_node_id: str
        relationship_name: str

    class KnowledgeGraph(BaseModel):
        """Knowledge graph."""

        summary: str
        description: str
        nodes: List[Node] = Field(..., default_factory=list)
        edges: List[Edge] = Field(..., default_factory=list)
else:

    class Node(BaseModel):
        """Node in a knowledge graph."""

        id: str
        name: str
        type: str
        description: str

    class Edge(BaseModel):
        """Edge in a knowledge graph."""

        source_node_id: str
        target_node_id: str
        relationship_name: str

    class KnowledgeGraph(BaseModel):
        """Knowledge graph."""

        nodes: List[Node] = Field(..., default_factory=list)
        edges: List[Edge] = Field(..., default_factory=list)


class GraphQLQuery(BaseModel):
    """GraphQL query."""

    query: str


class Answer(BaseModel):
    """Answer."""

    answer: str


class ChunkStrategy(Enum):
    EXACT = "exact"
    PARAGRAPH = "paragraph"
    SENTENCE = "sentence"
    CODE = "code"
    LANGCHAIN_CHARACTER = "langchain_character"


class ChunkEngine(Enum):
    LANGCHAIN_ENGINE = "langchain"
    DEFAULT_ENGINE = "default"
    HAYSTACK_ENGINE = "haystack"


class MemorySummary(BaseModel):
    """Memory summary."""

    nodes: List[Node] = Field(..., default_factory=list)
    edges: List[Edge] = Field(..., default_factory=list)


class TextSubclass(str, Enum):
    ARTICLES = "Articles, essays, and reports"
    BOOKS = "Books and manuscripts"
    NEWS_STORIES = "News stories and blog posts"
    RESEARCH_PAPERS = "Research papers and academic publications"
    SOCIAL_MEDIA = "Social media posts and comments"
    WEBSITE_CONTENT = "Website content and product descriptions"
    PERSONAL_NARRATIVES = "Personal narratives and stories"
    SPREADSHEETS = "Spreadsheets and tables"
    FORMS = "Forms and surveys"
    DATABASES = "Databases and CSV files"
    SOURCE_CODE = "Source code in various programming languages"
    SHELL_SCRIPTS = "Shell commands and scripts"
    MARKUP_LANGUAGES = "Markup languages (HTML, XML)"
    STYLESHEETS = "Stylesheets (CSS) and configuration files (YAML, JSON, INI)"
    CHAT_TRANSCRIPTS = "Chat transcripts and messaging history"
    CUSTOMER_SERVICE_LOGS = "Customer service logs and interactions"
    CONVERSATIONAL_AI = "Conversational AI training data"
    TEXTBOOK_CONTENT = "Textbook content and lecture notes"
    EXAM_QUESTIONS = "Exam questions and academic exercises"
    E_LEARNING_MATERIALS = "E-learning course materials"
    POETRY = "Poetry and prose"
    SCRIPTS = "Scripts for plays, movies, and television"
    SONG_LYRICS = "Song lyrics"
    MANUALS = "Manuals and user guides"
    TECH_SPECS = "Technical specifications and API documentation"
    HELPDESK_ARTICLES = "Helpdesk articles and FAQs"
    LEGAL_CONTRACTS = "Contracts and agreements"
    LAWS = "Laws, regulations, and legal case documents"
    POLICY_DOCUMENTS = "Policy documents and compliance materials"
    CLINICAL_TRIALS = "Clinical trial reports"
    PATIENT_RECORDS = "Patient records and case notes"
    SCIENTIFIC_ARTICLES = "Scientific journal articles"
    FINANCIAL_REPORTS = "Financial reports and statements"
    BUSINESS_PLANS = "Business plans and proposals"
    MARKET_RESEARCH = "Market research and analysis reports"
    AD_COPIES = "Ad copies and marketing slogans"
    PRODUCT_CATALOGS = "Product catalogs and brochures"
    PRESS_RELEASES = "Press releases and promotional content"
    PROFESSIONAL_EMAILS = "Professional and formal correspondence"
    PERSONAL_EMAILS = "Personal emails and letters"
    IMAGE_CAPTIONS = "Image and video captions"
    ANNOTATIONS = "Annotations and metadata for various media"
    VOCAB_LISTS = "Vocabulary lists and grammar rules"
    LANGUAGE_EXERCISES = "Language exercises and quizzes"
    LEGAL_AND_REGULATORY_DOCUMENTS = "Legal and Regulatory Documents"
    OTHER_TEXT = "Other types of text data"


class AudioSubclass(str, Enum):
    MUSIC_TRACKS = "Music tracks and albums"
    PODCASTS = "Podcasts and radio broadcasts"
    AUDIOBOOKS = "Audiobooks and audio guides"
    INTERVIEWS = "Recorded interviews and speeches"
    SOUND_EFFECTS = "Sound effects and ambient sounds"
    OTHER_AUDIO = "Other types of audio recordings"


class ImageSubclass(str, Enum):
    PHOTOGRAPHS = "Photographs and digital images"
    ILLUSTRATIONS = "Illustrations, diagrams, and charts"
    INFOGRAPHICS = "Infographics and visual data representations"
    ARTWORK = "Artwork and paintings"
    SCREENSHOTS = "Screenshots and graphical user interfaces"
    OTHER_IMAGES = "Other types of images"


class VideoSubclass(str, Enum):
    MOVIES = "Movies and short films"
    DOCUMENTARIES = "Documentaries and educational videos"
    TUTORIALS = "Video tutorials and how-to guides"
    ANIMATED_FEATURES = "Animated features and cartoons"
    LIVE_EVENTS = "Live event recordings and sports broadcasts"
    OTHER_VIDEOS = "Other types of video content"


class MultimediaSubclass(str, Enum):
    WEB_CONTENT = "Interactive web content and games"
    VR_EXPERIENCES = "Virtual reality (VR) and augmented reality (AR) experiences"
    MIXED_MEDIA = "Mixed media presentations and slide decks"
    E_LEARNING_MODULES = "E-learning modules with integrated multimedia"
    DIGITAL_EXHIBITIONS = "Digital exhibitions and virtual tours"
    OTHER_MULTIMEDIA = "Other types of multimedia content"


class Model3DSubclass(str, Enum):
    ARCHITECTURAL_RENDERINGS = "Architectural renderings and building plans"
    PRODUCT_MODELS = "Product design models and prototypes"
    ANIMATIONS = "3D animations and character models"
    SCIENTIFIC_VISUALIZATIONS = "Scientific simulations and visualizations"
    VR_OBJECTS = "Virtual objects for AR/VR applications"
    OTHER_3D_MODELS = "Other types of 3D models"


class ProceduralSubclass(str, Enum):
    TUTORIALS_GUIDES = "Tutorials and step-by-step guides"
    WORKFLOW_DESCRIPTIONS = "Workflow and process descriptions"
    SIMULATIONS = "Simulation and training exercises"
    RECIPES = "Recipes and crafting instructions"
    OTHER_PROCEDURAL = "Other types of procedural content"


class ContentType(BaseModel):
    """Base class for different types of content."""

    type: str


class TextContent(ContentType):
    type: str = "TEXTUAL_DOCUMENTS_USED_FOR_GENERAL_PURPOSES"
    subclass: List[TextSubclass]


class AudioContent(ContentType):
    type: str = "AUDIO_DOCUMENTS_USED_FOR_GENERAL_PURPOSES"
    subclass: List[AudioSubclass]


class ImageContent(ContentType):
    type: str = "IMAGE_DOCUMENTS_USED_FOR_GENERAL_PURPOSES"
    subclass: List[ImageSubclass]


class VideoContent(ContentType):
    type: str = "VIDEO_DOCUMENTS_USED_FOR_GENERAL_PURPOSES"
    subclass: List[VideoSubclass]


class MultimediaContent(ContentType):
    type: str = "MULTIMEDIA_DOCUMENTS_USED_FOR_GENERAL_PURPOSES"
    subclass: List[MultimediaSubclass]


class Model3DContent(ContentType):
    type: str = "3D_MODEL_DOCUMENTS_USED_FOR_GENERAL_PURPOSES"
    subclass: List[Model3DSubclass]


class ProceduralContent(ContentType):
    type: str = "PROCEDURAL_DOCUMENTS_USED_FOR_GENERAL_PURPOSES"
    subclass: List[ProceduralSubclass]


class DefaultContentPrediction(BaseModel):
    """Class for a single class label prediction."""

    label: Union[
        TextContent,
        AudioContent,
        ImageContent,
        VideoContent,
        MultimediaContent,
        Model3DContent,
        ProceduralContent,
    ]


class SummarizedContent(BaseModel):
    """Class for a single class label summary and description."""

    summary: str
    description: str


class SummarizedFunction(BaseModel):
    name: str
    description: str
    inputs: Optional[List[str]] = None
    outputs: Optional[List[str]] = None
    decorators: Optional[List[str]] = None


class SummarizedClass(BaseModel):
    name: str
    description: str
    methods: Optional[List[SummarizedFunction]] = None
    decorators: Optional[List[str]] = None


class SummarizedCode(BaseModel):
    high_level_summary: str
    key_features: List[str]
    imports: List[str] = []
    constants: List[str] = []
    classes: List[SummarizedClass] = []
    functions: List[SummarizedFunction] = []
    workflow_description: Optional[str] = None


class GraphDBType(Enum):
    NETWORKX = auto()
    NEO4J = auto()
    FALKORDB = auto()
    KUZU = auto()


# Models for representing different entities
class Relationship(BaseModel):
    type: str
    source: Optional[str] = None
    target: Optional[str] = None
    properties: Optional[Dict[str, Any]] = None


class DocumentType(BaseModel):
    type_id: str
    description: str
    default_relationship: Relationship = Relationship(type="is_type")


class Category(BaseModel):
    category_id: str
    name: str
    default_relationship: Relationship = Relationship(type="categorized_as")


class Document(BaseModel):
    id: str
    type: str
    title: str


class UserLocation(BaseModel):
    location_id: str
    description: str
    default_relationship: Relationship = Relationship(type="located_in")


class UserProperties(BaseModel):
    custom_properties: Optional[Dict[str, Any]] = None
    location: Optional[UserLocation] = None


class DefaultGraphModel(BaseModel):
    node_id: str
    user_properties: UserProperties = UserProperties()
    documents: List[Document] = []
    default_fields: Optional[Dict[str, Any]] = {}
    default_relationship: Relationship = Relationship(type="has_properties")


class ChunkSummary(BaseModel):
    text: str
    chunk_id: str


class ChunkSummaries(BaseModel):
    """Relevant summary and chunk id"""

    summaries: List[ChunkSummary]
