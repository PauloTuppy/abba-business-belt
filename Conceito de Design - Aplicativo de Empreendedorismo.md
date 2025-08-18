# Conceito de Design - Aplicativo de Empreendedorismo

## Visão Geral
O aplicativo será uma plataforma web moderna e intuitiva para empreendedores, com foco em gamificação através de um sistema de faixas que evolui conforme o progresso do usuário.

## Sistema de Faixas e Paleta de Cores

### Faixa Branca (Iniciante)
- **Cor Principal**: #FFFFFF (Branco)
- **Cor Secundária**: #F8F9FA (Cinza muito claro)
- **Cor de Destaque**: #6C757D (Cinza médio)
- **Texto**: #212529 (Preto suave)

### Faixa Amarela
- **Cor Principal**: #FFF3CD (Amarelo claro)
- **Cor Secundária**: #FFEB3B (Amarelo)
- **Cor de Destaque**: #FF9800 (Laranja)
- **Texto**: #856404 (Marrom escuro)

### Faixa Laranja
- **Cor Principal**: #FFE0B2 (Laranja claro)
- **Cor Secundária**: #FF9800 (Laranja)
- **Cor de Destaque**: #F57C00 (Laranja escuro)
- **Texto**: #E65100 (Laranja muito escuro)

### Faixa Verde
- **Cor Principal**: #D4EDDA (Verde claro)
- **Cor Secundária**: #4CAF50 (Verde)
- **Cor de Destaque**: #2E7D32 (Verde escuro)
- **Texto**: #155724 (Verde muito escuro)

### Faixa Azul
- **Cor Principal**: #CCE5FF (Azul claro)
- **Cor Secundária**: #2196F3 (Azul)
- **Cor de Destaque**: #1976D2 (Azul escuro)
- **Texto**: #0D47A1 (Azul muito escuro)

### Faixa Roxa
- **Cor Principal**: #E1BEE7 (Roxo claro)
- **Cor Secundária**: #9C27B0 (Roxo)
- **Cor de Destaque**: #7B1FA2 (Roxo escuro)
- **Texto**: #4A148C (Roxo muito escuro)

### Faixa Marrom
- **Cor Principal**: #D7CCC8 (Marrom claro)
- **Cor Secundária**: #795548 (Marrom)
- **Cor de Destaque**: #5D4037 (Marrom escuro)
- **Texto**: #3E2723 (Marrom muito escuro)

### Faixa Preta (Avançado)
- **Cor Principal**: #212529 (Preto suave)
- **Cor Secundária**: #343A40 (Cinza escuro)
- **Cor de Destaque**: #FFC107 (Dourado)
- **Texto**: #FFFFFF (Branco)

## Tipografia

### Fonte Principal
- **Família**: Inter, system-ui, sans-serif
- **Títulos H1**: 2.5rem (40px), peso 700
- **Títulos H2**: 2rem (32px), peso 600
- **Títulos H3**: 1.5rem (24px), peso 600
- **Corpo**: 1rem (16px), peso 400
- **Pequeno**: 0.875rem (14px), peso 400

## Layout e Estrutura

### Header
- Logo do aplicativo à esquerda
- Indicador de faixa atual (visual de faixa colorida)
- Menu de navegação principal
- Avatar do usuário e configurações

### Sidebar (Desktop)
- Navegação principal com ícones
- Progresso da faixa atual
- Acesso rápido às funcionalidades principais

### Dashboard Principal
- Cards informativos com métricas
- Gráficos e visualizações de dados
- Acesso rápido às ferramentas principais
- Feed de atividades recentes

### Abas de Conteúdo
1. **Marketing**: Estratégias e ferramentas
2. **Mindset**: Desenvolvimento pessoal
3. **Mídias Sociais**: YouTube e Instagram
4. **Dieta**: Nutrição e estratégias alimentares
5. **Finanças**: Análise financeira e planejamento

## Elementos Visuais

### Ícones
- Estilo: Outline/Linear
- Tamanho padrão: 24px
- Cores: Seguem a paleta da faixa atual

### Botões
- **Primário**: Cor de destaque da faixa atual
- **Secundário**: Cor secundária da faixa atual
- **Bordas**: Arredondadas (8px)
- **Hover**: Escurecimento de 10%

### Cards
- **Sombra**: 0 2px 8px rgba(0,0,0,0.1)
- **Bordas**: Arredondadas (12px)
- **Padding**: 24px
- **Background**: Branco ou cor principal da faixa

### Animações
- **Transições**: 0.3s ease-in-out
- **Hover effects**: Suaves e responsivos
- **Loading states**: Skeleton screens
- **Micro-interações**: Feedback visual imediato

## Responsividade

### Desktop (1200px+)
- Layout com sidebar fixa
- 3-4 colunas de cards
- Navegação horizontal completa

### Tablet (768px - 1199px)
- Sidebar colapsável
- 2-3 colunas de cards
- Navegação adaptada

### Mobile (< 768px)
- Menu hambúrguer
- Layout de coluna única
- Navegação bottom tab
- Gestos touch otimizados

## Acessibilidade

- Contraste mínimo WCAG AA
- Navegação por teclado
- Screen reader friendly
- Textos alternativos em imagens
- Foco visível em elementos interativos

## Gamificação Visual

### Indicador de Progresso
- Barra de progresso circular
- Porcentagem de conclusão
- Próximos objetivos visíveis

### Conquistas
- Badges visuais
- Animações de celebração
- Histórico de conquistas

### Sistema de Pontos
- Contador visível
- Histórico de ganhos
- Metas claras para próxima faixa

