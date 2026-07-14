import type { Site, Metadata, Socials } from "@types";

export const SITE: Site = {
  NAME: "Ilya Voytov",
  EMAIL: "ilya@voytov.com",
  NUM_POSTS_ON_HOMEPAGE: 3,
  NUM_WORKS_ON_HOMEPAGE: 3,
  NUM_PROJECTS_ON_HOMEPAGE: 0,
};

export const HOME: Metadata = {
  TITLE: "Ilya Voytov",
  DESCRIPTION: "Quant Research at Lazard",
};

export const BLOG: Metadata = {
  TITLE: "Blog",
  DESCRIPTION: "Writing by Ilya Voytov.",
};

export const WORK: Metadata = {
  TITLE: "Work",
  DESCRIPTION: "Where I have worked and what I have done.",
};

export const PROJECTS: Metadata = {
  TITLE: "Projects",
  DESCRIPTION: "A collection of my projects, with links to repositories and demos.",
};

export const SOCIALS: Socials = [
  { NAME: "threads", HREF: "https://www.threads.com/@goilya" },
  { NAME: "github", HREF: "https://github.com/ivoytov" },
  { NAME: "linkedin", HREF: "https://www.linkedin.com/in/voytov/" },
];
