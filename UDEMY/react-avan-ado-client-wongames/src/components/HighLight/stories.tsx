import { Story, Meta } from '@storybook/react'
import HighLight, { HighLightProps } from '.'

export default {
  title: 'Highlight',
  component: HighLight,
  args: {
    title: 'Read Dead is back!',
    subtitle: 'Come see John’s new adventures',
    backgroundImage: '/img/red-dead-img.jpg',
    buttonLabel: 'Buy now',
    buttonLink: '/games/rdr2'
  }
} as Meta

export const Default: Story<HighLightProps> = (args) => (
  <div style={{ maxWidth: '104rem' }}>
    <HighLight {...args} />
  </div>
)

export const WithFloatImage: Story<HighLightProps> = (args) => (
  <div style={{ maxWidth: '104rem' }}>
    <HighLight {...args} />
  </div>
)

WithFloatImage.args = {
  floatImage: '/img/Image.png'
}
