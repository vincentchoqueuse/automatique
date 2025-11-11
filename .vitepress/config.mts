import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "automatique",
  description: "A VitePress Site",
  base: '/automatique/',
  srcExclude: ['**/README.md', '**/temp'],
  markdown: {
    math: true
  },
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    editLink: {
      pattern: 'https://github.com/vincentchoqueuse/automatique/issues',
      text: 'Suggest any modification on GitLab'
    },
    logo: '/logo.png',
    search: {
      provider: 'local'
    },
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Cours', link: '/content/course/', activeMatch: '/content/course/'},
      { text: 'Tutorial', link: '/content/tutorial/', activeMatch: '/content/tutorial/'},
      { text: 'Annexes', link: '/content/appendix/', activeMatch: '/content/appendix/'},
    ],

    sidebar: {
      '/content/': [
      {
        text: 'Introduction',
        items: [
          { text: "Acquis d'Apprentissage Visés", link: '/content/course/00_introduction/01_aav/'},
          { text: "Objectifs", link: '/content/course/00_introduction/02_objectives/'},
        ]
      },
      {
        text: 'AAV1 : Modélisation, analyse et identification des SLIT',
        items: [
          { text: 'Contexte & Hypothèses', link: '/content/course/01_slit/01_context/'},
          { text: 'Analyse des SLIT', link: '/content/course/01_slit/02_analysis/'},
          { text: 'Transformée de Laplace', link: '/content/course/01_slit/03_laplace/' },
          { text: 'Systèmes de Premier Ordre', link: '/content/course/01_slit/04_first_order/' },
          { text: 'Systèmes de Second Ordre', link: '/content/course/01_slit/05_second_order/' },
          { text: 'Examples', link: '/content/course/01_slit/06_examples/' },
        ]
      },
      {
        text: 'AAV2 : Analyse des systèmes en boucle fermée',
        link: '/content/course/02_closed_loop/',
        items: [
          { text: 'Contexte & Hypothèses', link: '/content/course/02_closed_loop/01_context/'},
          { text: 'Stabilité en BF', link: '/content/course/02_closed_loop/02_stability/' },
          { text: 'Performances Statiques', link: '/content/course/02_closed_loop/03_static/' },
          { text: 'Performances Dynamiques', link: '/content/course/02_closed_loop/04_dynamic/' },
        ]
      },
      {
        text: 'AA3 : Synthèse fréquentielle de correcteurs linéaires',
        link: '/content/course/03_controller/',
        items: [
          { text: 'Liste des Correcteurs', link: '/content/course/03_controller/01_usual/' },
        ]
      }
      ],
      '/content/appendix/': [
            {
              text: 'Annexes',
              items: [
                { text: 'Table des Transformées', link: '/content/appendix/table/' },
                { text: 'Liste des circuits', link: '/content/appendix/circuit_list/' },
                { text: "Rappels d'Electronique", link: '/content/appendix/circuit_analysis/' }
              ]
            }
        ],
      '/content/tutorial/': [
      {
        text: 'Tutorial',
        items: [
          { text: 'Installation', link: '/content/tutorial/01_installation' },
          { text: 'Calcul de la Réponse Indicielle', link: '/content/tutorial/02_calcul_comparaison' },
          { text: 'Utilisation de Python (step)', link: '/content/tutorial/03_python_step_response' },
          { text: 'Python Cheatsheet', link: '/content/tutorial/04_python_cheatsheet'}
        ]
      }]
    }
    ,
    socialLinks: [
      { icon: 'github', link: 'https://github.com/vincentchoqueuse/automatique' }
    ]
  }
})
