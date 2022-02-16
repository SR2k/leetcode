/* eslint-disable import/no-extraneous-dependencies */
import yargsParser from 'yargs-parser'
import { createFile, readdir, writeFile } from 'fs-extra'
import { resolve } from 'path'
import { stat } from 'fs'

const fileExists = (file: string) => new Promise((res, rej) => {
  stat(file, (err) => {
    if (err == null) {
      res(true)
    } else if (err.code === 'ENOENT') {
      // file does not exist
      res(false)
    } else {
      rej(err)
    }
  })
});

(async () => {
  const argv = yargsParser(process.argv.slice(2))

  const id: number = +(argv._?.[0] || NaN)
  if (!id) throw new Error('Invalid ID')

  const files = await readdir(__dirname)
  const file = files.find((f) => f.startsWith(`${id}.`) && f.endsWith('.ts'))
  if (!file) throw new Error('File doesn\'t exits')

  const problemName = file.replace(/\.ts$/, '')
  const newFileName = resolve(__dirname, `./tests/${problemName}.test.ts`)

  if (await fileExists(newFileName)) {
    throw new Error(`${newFileName} already exists`)
  }

  await createFile(newFileName)
  await writeFile(newFileName, `import {  } from '../${problemName}'

describe('${problemName}', () => {
  it('should work', () => {
    
  })
})
`)
})()
